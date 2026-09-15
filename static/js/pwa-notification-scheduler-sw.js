/**
 * Service worker: PWA local notification checks (importScripts from service-worker.js).
 * Reads prefs from IndexedDB; does not use localStorage.
 */
/* global DiariPwaNotificationIdb, DiariPwaNotificationTemplates */
'use strict';

const NOTIFY_TZ = 'Asia/Manila';
const CHECK_TAG_DAILY = 'diari-pwa-daily-reminder';
const CHECK_TAG_INSIGHT = 'diari-pwa-insight-followup';
const CHECK_TAG_STREAK_1HR = 'diari-pwa-streak-1hr';
const CHECK_TAG_STREAK_30MIN = 'diari-pwa-streak-30min';

/** Asia/Manila — PWA streak reminders at 9:00 PM and 11:00 PM. */
const STREAK_REMINDER_FIRST = { h: 21, m: 0 };
const STREAK_REMINDER_SECOND = { h: 23, m: 0 };

function manilaDateKey(d) {
    return new Intl.DateTimeFormat('en-CA', {
        timeZone: NOTIFY_TZ,
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
    }).format(d || new Date());
}

function manilaHourMinute(d) {
    const parts = new Intl.DateTimeFormat('en-GB', {
        timeZone: NOTIFY_TZ,
        hour: '2-digit',
        minute: '2-digit',
        hourCycle: 'h23',
    }).formatToParts(d || new Date());
    const h = Number(parts.find((p) => p.type === 'hour')?.value || 0);
    const m = Number(parts.find((p) => p.type === 'minute')?.value || 0);
    return { h, m };
}

function parseHHmm(s) {
    const m = /^(\d{2}):(\d{2})$/.exec(String(s || '').trim());
    if (!m) return null;
    return { h: Number(m[1]), m: Number(m[2]) };
}

const REMINDER_WINDOW_MINUTES = 15;

function isSameMinute(nowH, nowM, targetH, targetM) {
    return nowH === targetH && nowM === targetM;
}

function isInReminderWindow(nowH, nowM, targetH, targetM, windowMinutes) {
    const w = Math.max(1, windowMinutes || REMINDER_WINDOW_MINUTES);
    const now = nowH * 60 + nowM;
    const start = targetH * 60 + targetM;
    return now >= start && now < start + w;
}

function entryDayKeyManila(iso) {
    if (!iso) return '';
    const d = new Date(iso);
    if (Number.isNaN(d.getTime())) return '';
    return manilaDateKey(d);
}

function sortEntries(entries) {
    return (entries || [])
        .filter((e) => e && (e.date || e.createdAt))
        .slice()
        .sort((a, b) => {
            const ta = new Date(a.date || a.createdAt).getTime();
            const tb = new Date(b.date || b.createdAt).getTime();
            return tb - ta;
        });
}

function hasEntryToday(entries) {
    const today = manilaDateKey(new Date());
    return sortEntries(entries).some((e) => entryDayKeyManila(e.date || e.createdAt) === today);
}

function computeStreakCount(entries) {
    try {
        const ds = self.DiariStreak;
        if (ds && typeof ds.computeEntryStreak === 'function') {
            return ds.computeEntryStreak(entries || []).streak || 0;
        }
    } catch (_) {
        /* ignore */
    }
    return 0;
}

function getLastEntry(entries) {
    return sortEntries(entries)[0] || null;
}

function resolveFeeling(entry) {
    return String(entry?.emotionLabel || entry?.feeling || 'neutral').toLowerCase();
}

function entryTitleSnippet(entry) {
    const title = String(entry?.title || '').trim();
    if (title) return title.slice(0, 60);
    const text = String(entry?.text || '').trim();
    if (!text) return 'your last entry';
    return text.split('\n')[0].slice(0, 60);
}

function msSinceEntry(entry) {
    const d = new Date(entry?.date || entry?.createdAt || 0);
    return Date.now() - d.getTime();
}

function shouldFireInsightFollowup(prefs, lastEntry) {
    if (!prefs.insightFollowupsEnabled) return false;
    if (!lastEntry || lastEntry.id == null) return false;
    const entryKey = String(lastEntry.id);
    if (prefs.lastInsightEntryId === entryKey && prefs.lastInsightDateKey === manilaDateKey(new Date())) {
        return false;
    }
    const elapsed = msSinceEntry(lastEntry);
    const fourHours = 4 * 60 * 60 * 1000;
    const minDelay = 45 * 60 * 1000;
    if (elapsed < minDelay) return false;
    if (elapsed >= fourHours && elapsed < 36 * 60 * 60 * 1000) return true;
    const { h, m } = manilaHourMinute(new Date());
    if (h === 10 && m === 0 && entryDayKeyManila(lastEntry.date || lastEntry.createdAt) !== manilaDateKey(new Date())) {
        return true;
    }
    return false;
}

async function showLocalNotification(registration, title, body, tag, url) {
    if (!registration || typeof registration.showNotification !== 'function') return false;
    try {
        await registration.showNotification(title, {
            body,
            tag,
            renotify: true,
            icon: '/diariclogo-pwa-notif-192.png',
            badge: '/diariclogo.png',
            data: { url: url || '/dashboard.html' },
        });
        return true;
    } catch (e) {
        console.warn('[PWA SW] showNotification failed:', e);
        return false;
    }
}

/**
 * Local-first daily reminder: when the app is open this fires on time even if
 * the server push is delayed by FCM/Doze. Uses the SAME tag as the server push
 * so a late server arrival silently replaces it instead of stacking a duplicate.
 * Posts a delivery-ack so the server stops retrying.
 */
async function showLocalDailyReminder(registration, body) {
    if (!registration || typeof registration.showNotification !== 'function') return false;
    const tag = 'diari-daily-reminder';
    try {
        let existing = [];
        try {
            existing = (await registration.getNotifications({ tag })) || [];
        } catch (_) {
            existing = [];
        }
        if (existing.length) {
            // Server push already showing — adopt it (no re-buzz), just ack below.
        } else {
            await registration.showNotification('A gentle journal nudge', {
                body,
                tag,
                renotify: true,
                icon: '/diariclogo-pwa-notif-192.png',
                badge: '/diariclogo.png',
                vibrate: [300, 100, 300, 100, 300],
                data: { url: '/dashboard.html', tag },
            });
        }
    } catch (e) {
        console.warn('[PWA SW] local daily showNotification failed:', e);
        return false;
    }
    try {
        fetch('/api/push/delivery-ack', {
            method: 'POST',
            credentials: 'include',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                tag,
                title: 'A gentle journal nudge',
                receivedAt: new Date().toISOString(),
                source: 'local',
            }),
        }).catch(() => {});
    } catch (_) {
        /* ignore */
    }
    return true;
}

async function runNotificationChecks() {
    const idb = self.DiariPwaNotificationIdb;
    const tpl = self.DiariPwaNotificationTemplates;
    if (!idb || !tpl) return;

    let prefs;
    try {
        prefs = await idb.readPrefs();
    } catch (e) {
        console.warn('[PWA SW] readPrefs failed:', e);
        return;
    }
    if (!prefs || !prefs.pwaOnly) return;
    if (prefs.permission !== 'granted') return;

    const registration = self.registration;
    const now = new Date();
    const todayKey = manilaDateKey(now);
    const { h, m } = manilaHourMinute(now);
    const entries = Array.isArray(prefs.entries) ? prefs.entries : [];
    const reminder = parseHHmm(prefs.reminderHHmm || '09:00');

  // Local-first: when the app is open this fires on time even if the server
  // push is delayed by FCM/Doze. Same tag as the server push, so a late
  // server arrival silently replaces it instead of stacking a duplicate.
    if (
        prefs.dailyRemindersEnabled &&
        reminder &&
        isInReminderWindow(h, m, reminder.h, reminder.m, REMINDER_WINDOW_MINUTES) &&
        prefs.lastDailyReminderDateKey !== todayKey &&
        !hasEntryToday(entries)
    ) {
        const body = tpl.buildDailyReminderBody();
        const ok = await showLocalDailyReminder(
            registration,
            body
        );
        if (ok) {
            prefs.lastDailyReminderDateKey = todayKey;
            await idb.writePrefs(prefs);
        }
    }

    const streakRemindersOn =
        prefs.streakRemindersEnabled !== false &&
        (prefs.dailyRemindersEnabled === true);
    if (streakRemindersOn && !hasEntryToday(entries)) {
        const streak = computeStreakCount(entries);
        if (streak > 0 && typeof tpl.buildStreakReminderBody === 'function') {
            if (
                isSameMinute(h, m, STREAK_REMINDER_FIRST.h, STREAK_REMINDER_FIRST.m) &&
                prefs.lastStreak1hrDateKey !== todayKey
            ) {
                const body1 = tpl.buildStreakReminderBody('1hr', streak);
                const ok1 = await showLocalNotification(
                    registration,
                    'Your streak tonight',
                    body1,
                    CHECK_TAG_STREAK_1HR,
                    '/dashboard.html'
                );
                if (ok1) {
                    prefs.lastStreak1hrDateKey = todayKey;
                    await idb.writePrefs(prefs);
                }
            }
            if (
                isSameMinute(h, m, STREAK_REMINDER_SECOND.h, STREAK_REMINDER_SECOND.m) &&
                prefs.lastStreak30minDateKey !== todayKey
            ) {
                const body2 = tpl.buildStreakReminderBody('30min', streak);
                const ok2 = await showLocalNotification(
                    registration,
                    'Before the day ends',
                    body2,
                    CHECK_TAG_STREAK_30MIN,
                    '/dashboard.html'
                );
                if (ok2) {
                    prefs.lastStreak30minDateKey = todayKey;
                    await idb.writePrefs(prefs);
                }
            }
        }
    }

    const lastEntry = getLastEntry(entries);
    if (shouldFireInsightFollowup(prefs, lastEntry)) {
        const mood = resolveFeeling(lastEntry);
        const body = tpl.buildInsightNotificationBody({
            mood,
            tone: tpl.reflectiveTone ? tpl.reflectiveTone(mood) : undefined,
            title: entryTitleSnippet(lastEntry),
            snippet: entryTitleSnippet(lastEntry),
        });
        const ok = await showLocalNotification(
            registration,
            'Following up on your journal',
            body,
            CHECK_TAG_INSIGHT + '-' + String(lastEntry.id),
            '/entries.html'
        );
        if (ok) {
            prefs.lastInsightEntryId = String(lastEntry.id);
            prefs.lastInsightDateKey = todayKey;
            await idb.writePrefs(prefs);
        }
    }
}

/* push + notificationclick handlers live in /service-worker.js (always loaded) */

self.addEventListener('message', (event) => {
    const data = event.data || {};
    if (data.type === 'DIARI_PWA_CHECK_NOTIFICATIONS') {
        event.waitUntil(runNotificationChecks());
    }
});

self.addEventListener('periodicsync', (event) => {
    if (event.tag === 'diari-pwa-notification-check') {
        event.waitUntil(runNotificationChecks());
    }
});

self.addEventListener('sync', (event) => {
    if (event.tag === 'diari-pwa-notification-check') {
        event.waitUntil(runNotificationChecks());
    }
});
