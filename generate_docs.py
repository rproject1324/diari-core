#!/usr/bin/env python3
"""DiariCore Comprehensive System Documentation - PDF Generator"""
from fpdf import FPDF
import os

class DiariCoreDocs(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
        self.chapter_num = 0
        self.in_toc = False
        self.set_left_margin(20)
        self.set_right_margin(20)

    def header(self):
        if self.page_no() > 1 and not self.in_toc:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "DiariCore - Comprehensive System Documentation", align="L")
            self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(180, 180, 180)
            self.line(20, self.get_y(), 190, self.get_y())
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150, 150, 150)
        if self.page_no() == 1:
            return
        self.cell(0, 10, "DiariCore Documentation v1.0  |  Generated 2026", align="C")

    def title_page(self):
        self.add_page()
        self.ln(50)
        self.set_font("Helvetica", "B", 36)
        self.set_text_color(50, 80, 65)
        self.cell(0, 18, "DiariCore", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self.set_font("Helvetica", "", 16)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, "Comprehensive System Documentation", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.set_draw_color(111, 143, 127)
        self.set_line_width(0.8)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(12)
        self.set_font("Helvetica", "", 12)
        self.set_text_color(80, 80, 80)
        for line in [
            "A Progressive Web App for Mindful Journaling",
            "with ML-Based Emotion & Sentiment Analysis",
            "", "Version 1.0  |  August 2026",
        ]:
            self.cell(0, 8, line, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(20)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 7, "Project Members:", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "B", 10)
        for name in ["Tolentino, Lawrence Dave P.", "Tolentino, Cathlene A.", "Valenzuela, John Oliver R."]:
            self.cell(0, 7, name, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 7, "Live: https://diaricore.up.railway.app/", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 7, "GitHub: https://github.com/lproject012125/diari-core", align="C", new_x="LMARGIN", new_y="NEXT")

    def toc_page(self):
        self.add_page()
        self.in_toc = True
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(50, 80, 65)
        self.cell(0, 12, "Table of Contents", new_x="LMARGIN", new_y="NEXT")
        self.ln(6)
        self.set_draw_color(111, 143, 127)
        self.set_line_width(0.5)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(6)
        for num, title in [
            ("1.", "Introduction & Project Overview"),
            ("2.", "System Architecture"),
            ("3.", "Database Design"),
            ("4.", "API Reference"),
            ("5.", "Authentication & Security"),
            ("6.", "Machine Learning Pipeline"),
            ("7.", "Progressive Web App (PWA)"),
            ("8.", "Push Notification System"),
            ("9.", "Frontend Pages & Templates"),
            ("10.", "Frontend JavaScript Modules"),
            ("11.", "Frontend CSS & Theming"),
            ("12.", "Deployment & Infrastructure"),
            ("13.", "Configuration & Environment Variables"),
            ("A.", "Complete API Endpoint Reference"),
            ("B.", "Database Table Definitions"),
        ]:
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(50, 50, 50)
            self.cell(12, 7, num)
            self.set_font("Helvetica", "", 10)
            self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.in_toc = False

    def chapter_title(self, title):
        self.chapter_num += 1
        self.add_page()
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(50, 80, 65)
        self.cell(0, 14, f"{self.chapter_num}. {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(111, 143, 127)
        self.set_line_width(0.5)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(8)
        self.set_text_color(40, 40, 40)

    def section_title(self, title):
        self.ln(4)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(70, 100, 80)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_text_color(40, 40, 40)

    def subsection_title(self, title):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(80, 80, 80)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        self.set_text_color(40, 40, 40)

    def body_text(self, text):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet_list(self, items):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(40, 40, 40)
        for item in items:
            self.cell(8, 5.5, "-")
            self.multi_cell(0, 5.5, item)
            self.ln(1)
        self.ln(1)

    def add_table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [170 / len(headers)] * len(headers)
        self.set_font("Helvetica", "B", 8.5)
        self.set_fill_color(111, 143, 127)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, fill=True, align="C")
        self.ln()
        self.set_font("Helvetica", "", 8)
        self.set_text_color(40, 40, 40)
        fill = False
        for row in rows:
            max_h = 7
            for i, cell in enumerate(row):
                lines = self.multi_cell(col_widths[i], 5, str(cell), split_only=True)
                h = max(7, len(lines) * 5)
                max_h = max(max_h, h)
            if self.get_y() + max_h > 270:
                self.add_page()
                self.set_font("Helvetica", "B", 8.5)
                self.set_fill_color(111, 143, 127)
                self.set_text_color(255, 255, 255)
                for i, h in enumerate(headers):
                    self.cell(col_widths[i], 7, h, border=1, fill=True, align="C")
                self.ln()
                self.set_font("Helvetica", "", 8)
                self.set_text_color(40, 40, 40)
            self.set_fill_color(240, 245, 242) if fill else self.set_fill_color(255, 255, 255)
            x_start = self.get_x()
            y_start = self.get_y()
            for i, cell in enumerate(row):
                x = x_start + sum(col_widths[:i])
                self.set_xy(x, y_start)
                self.multi_cell(col_widths[i], 5, str(cell), border=1, fill=fill, align="L")
            self.set_xy(x_start, y_start + max_h)
            fill = not fill
        self.ln(4)

    def code_block(self, code):
        self.set_font("Courier", "", 8)
        self.set_fill_color(245, 245, 245)
        self.set_text_color(50, 50, 50)
        for line in code.strip().split("\n"):
            if self.get_y() > 270:
                self.add_page()
            self.cell(0, 4.5, "  " + line, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(40, 40, 40)

    def note_box(self, text):
        self.set_fill_color(240, 248, 243)
        self.set_draw_color(111, 143, 127)
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(60, 80, 65)
        y = self.get_y()
        self.rect(20, y, 170, 12, style="DF")
        self.set_xy(24, y + 3)
        self.multi_cell(162, 5, text)
        self.set_y(y + 15)
        self.ln(2)

pdf = DiariCoreDocs()
pdf.set_title("DiariCore - Comprehensive System Documentation")
pdf.set_author("DiariCore Project Team")

pdf.title_page()
pdf.toc_page()

# CHAPTER 1
pdf.chapter_title("Introduction & Project Overview")
pdf.section_title("1.1 Project Description")
pdf.body_text(
    "DiariCore is a Progressive Web App (PWA) for mindful journaling. Users write private journal "
    "entries, tag their thoughts, and receive machine learning-based emotion and sentiment analysis "
    "to help them reflect on patterns in their wellbeing over time. The system combines secure account "
    "management, PostgreSQL storage, interactive insights charts, and personalized suggestions."
)
pdf.section_title("1.2 Key Features")
pdf.bullet_list([
    "Journal Entry Management: Create, view, edit, and delete entries with title, body text, custom tags, photos, and entry date/time.",
    "Custom Tags: Build personalized tags with icons from a searchable library to categorize entries.",
    "Emotion & Sentiment Analysis: Fine-tuned XLM-RoBERTa classifier (5 classes: angry, anxious, happy, neutral, sad) with confidence scores.",
    "Dashboard & Insights: Weekly mood trends, emotion breakdown charts, tag-based correlations, and journaling consistency metrics.",
    "Smart Suggestions: Supportive messages and activity recommendations based on recent emotional patterns.",
    "Secure Authentication: Registration with privacy consent, email OTP (Brevo), password reset, optional TOTP 2FA, session-based login.",
    "Progressive Web App (PWA): Installable on desktop and mobile with offline draft support and push notifications.",
    "Voice Transcription: Browser-based or server-side Whisper transcription for voice journal entries.",
    "Admin Tools: System settings, user management, analytics dashboard, service health monitoring, and audit logs.",
])
pdf.section_title("1.3 Project Team")
pdf.bullet_list([
    "Tolentino, Lawrence Dave P. - Lead Developer",
    "Tolentino, Cathlene A. - Team Member",
    "Valenzuela, John Oliver R. - Team Member",
])
pdf.section_title("1.4 Project Links")
pdf.add_table(
    ["Resource", "URL"],
    [
        ["Live App (Railway)", "https://diaricore.up.railway.app/"],
        ["Live App (AWS EC2)", "http://16.176.11.240/login.html"],
        ["GitHub Repository", "https://github.com/lproject012125/diari-core"],
        ["ML Model (HF Hub)", "https://huggingface.co/sseia/diari-core-mood/tree/main"],
        ["ML Inference Space", "https://huggingface.co/spaces/sseia/diaricore-inference/tree/main"],
    ],
    col_widths=[50, 120]
)

# CHAPTER 2
pdf.chapter_title("System Architecture")
pdf.section_title("2.1 High-Level Architecture")
pdf.body_text(
    "DiariCore follows a three-tier architecture with the Flask backend serving as the central hub. "
    "The frontend is a vanilla JavaScript SPA-like PWA that communicates with the Flask REST API. "
    "ML inference is offloaded to a separate Hugging Face Space to keep the web server lightweight."
)
pdf.subsection_title("Architecture Diagram")
pdf.code_block(
    "  [Browser / PWA]\n"
    "       |\n"
    "       | HTTP/REST (Fetch API)\n"
    "       v\n"
    "  [Flask App (Gunicorn)]\n"
    "       |         |           |\n"
    "       v         v           v\n"
    "  [PostgreSQL] [Brevo API] [HF Space]\n"
    "  (Railway)    (Email OTP)  (ML Inference)\n"
    "                      |\n"
    "               [HF Inference API]\n"
    "               (Voice Transcription)\n"
    "\n"
    "  [Push Notification Server]\n"
    "       |         |\n"
    "       v         v\n"
    "  [VAPID/FCM]  [Service Worker]\n"
    "  (pywebpush)  (Browser Push)"
)

pdf.section_title("2.2 Technology Stack")
pdf.add_table(
    ["Layer", "Technology", "Purpose"],
    [
        ["Frontend", "HTML5, CSS3, Vanilla JS (ES6+)", "UI rendering, PWA, offline support"],
        ["UI Framework", "Bootstrap 5", "Responsive layout, components"],
        ["Charts", "Chart.js", "Mood trends, emotion distribution"],
        ["Animations", "Lottie (lottie-web)", "Launch screen, success animations"],
        ["Backend", "Python 3, Flask", "REST API, session management"],
        ["WSGI Server", "Gunicorn", "Production HTTP server"],
        ["Database (Prod)", "PostgreSQL (Railway)", "Persistent data storage"],
        ["Database (Dev)", "SQLite", "Local development storage"],
        ["ML Model", "XLM-RoBERTa (ONNX)", "Emotion/sentiment classification"],
        ["ML Hosting", "Hugging Face Spaces", "Inference API (FastAPI + ONNX)"],
        ["Voice", "OpenAI Whisper (HF API)", "Speech-to-text transcription"],
        ["Email", "Brevo API", "OTP verification, password reset, 2FA recovery"],
        ["2FA", "pyotp (TOTP)", "Google Authenticator integration"],
        ["Push Notifications", "pywebpush (VAPID/FCM)", "Web Push delivery"],
        ["QR Codes", "segno", "TOTP setup QR generation"],
        ["Deployment", "Railway + AWS EC2", "Cloud hosting"],
    ],
    col_widths=[35, 55, 80]
)

pdf.section_title("2.3 File Structure Overview")
pdf.add_table(
    ["Path", "Description"],
    [
        ["app.py", "Main Flask application (3,232 lines) - all routes and API endpoints"],
        ["db.py", "Database schema, migrations, and query functions (3,653 lines)"],
        ["auth_security.py", "CSRF, rate limiting, login lockouts, OTP rate limiting"],
        ["password_policy.py", "Password validation rules and checklist"],
        ["input_security.py", "Input sanitization and validation functions"],
        ["space_nlp.py", "ML inference communication with Hugging Face Space"],
        ["hf_speech.py", "Voice/speech transcription via Hugging Face Inference API"],
        ["push_service.py", "Push notification sending, scheduling, subscription management"],
        ["push_scheduler.py", "Background daemon thread for push dispatch"],
        ["gunicorn.conf.py", "Gunicorn config with post_fork hook for push scheduler"],
        ["hf_space/app.py", "Hugging Face Space inference service (FastAPI + ONNX)"],
        ["templates/*.html", "14 HTML page templates"],
        ["static/js/*.js", "39 JavaScript modules"],
        ["static/css/*.css", "22 CSS stylesheets"],
        ["static/manifest.webmanifest", "PWA web app manifest"],
        ["static/service-worker.js", "PWA service worker"],
    ],
    col_widths=[55, 115]
)

# CHAPTER 3
pdf.chapter_title("Database Design")
pdf.section_title("3.1 Database Configuration")
pdf.body_text(
    "DiariCore supports dual database backends: PostgreSQL for production (via Railway) and SQLite for "
    "local development. The connection is determined by the DATABASE_URL environment variable. When set, "
    "psycopg2 connects to PostgreSQL; otherwise, SQLite is used with a local file (diaricore.db)."
)
pdf.section_title("3.2 Database Tables Overview")
pdf.body_text(
    "The database contains 14 tables covering user accounts, journal entries, authentication challenges, "
    "push notifications, and system settings. All tables are created and migrated via init_db() in db.py."
)
pdf.add_table(
    ["Table", "Primary Key", "Purpose"],
    [
        ["users", "id (SERIAL)", "User accounts: nickname, email, password_hash, avatar, TOTP, status"],
        ["pending_registrations", "email", "OTP-verified pending registrations with expiry"],
        ["password_resets", "email", "Password reset codes with expiry"],
        ["journal_entries", "id (SERIAL)", "Diary entries: title, text, tags, sentiment, emotion, images"],
        ["user_tags", "user_id + tag", "User-defined tags with optional icon names"],
        ["login_totp_challenges", "token", "Pending TOTP login challenges with expiry"],
        ["login_lockouts", "account_key", "Login failure tracking with lockout timers"],
        ["otp_resend_limits_*", "flow + identifier", "5 OTP rate limit tables"],
        ["login_totp_recovery_otps", "challenge_token", "TOTP recovery email codes"],
        ["user_password_change_challenges", "user_id", "Password change OTP with expiry"],
        ["user_profile_email_change_challenges", "user_id", "Email change OTP with pending payload"],
        ["admin_audit_logs", "id (SERIAL)", "Admin action audit trail with IP and timestamp"],
        ["push_subscriptions", "id (SERIAL)", "Web Push subscriptions per user per endpoint"],
        ["system_settings", "key", "Key-value system settings store"],
    ],
    col_widths=[55, 35, 80]
)

pdf.section_title("3.3 Key Table: journal_entries")
pdf.add_table(
    ["Column", "Type", "Description"],
    [
        ["id", "SERIAL PK", "Auto-incrementing entry ID"],
        ["user_id", "INT FK", "References users.id"],
        ["title", "VARCHAR(180)", "Entry title"],
        ["entry_datetime_utc", "TIMESTAMP", "Entry date/time in UTC"],
        ["text_content", "TEXT", "Journal entry body text"],
        ["tags_json", "JSONB", "Array of tag strings"],
        ["sentiment", "VARCHAR(12)", "positive, negative, or neutral"],
        ["emotion", "VARCHAR(12)", "happy, sad, anxious, angry, or neutral"],
        ["all_probs_json", "JSONB", "Probability distribution across 5 emotions"],
        ["image_urls_json", "JSONB", "Array of uploaded image URLs"],
        ["created_at", "TIMESTAMP", "Record creation timestamp"],
        ["updated_at", "TIMESTAMP", "Last modification timestamp"],
    ],
    col_widths=[45, 35, 90]
)

pdf.section_title("3.4 Key Table: users")
pdf.add_table(
    ["Column", "Type", "Description"],
    [
        ["id", "SERIAL PK", "Auto-incrementing user ID"],
        ["nickname", "VARCHAR(64) UNIQUE", "Username for login"],
        ["email", "VARCHAR(254) UNIQUE", "Email address"],
        ["password_hash", "TEXT", "Hashed password (werkzeug)"],
        ["first_name", "VARCHAR(64)", "User first name"],
        ["last_name", "VARCHAR(64)", "User last name"],
        ["gender", "VARCHAR(20)", "Male, Female, or Prefer not to say"],
        ["birthday", "DATE", "User birthday (YYYY-MM-DD)"],
        ["avatar_data_url", "TEXT", "Base64 JPEG profile photo"],
        ["ui_preferences_json", "JSONB", "Theme, palette, and UI settings"],
        ["totp_secret", "TEXT", "TOTP secret key (encrypted)"],
        ["totp_enabled", "BOOLEAN", "Whether 2FA is active"],
        ["is_disabled", "BOOLEAN", "Account disabled flag"],
        ["privacy_agreed_at", "TIMESTAMP", "Privacy consent timestamp"],
        ["last_login", "TIMESTAMP", "Last successful login"],
        ["created_at", "TIMESTAMP", "Account creation timestamp"],
    ],
    col_widths=[45, 40, 85]
)

pdf.section_title("3.5 Key Table: push_subscriptions")
pdf.add_table(
    ["Column", "Type", "Description"],
    [
        ["id", "SERIAL PK", "Auto-incrementing subscription ID"],
        ["user_id", "INT FK", "References users.id"],
        ["endpoint", "TEXT UNIQUE", "Push service endpoint URL"],
        ["subscription_json", "JSONB", "Full subscription object"],
        ["created_at", "TIMESTAMP", "Registration timestamp"],
        ["fcm_failures", "INTEGER", "Count of consecutive FCM delivery failures"],
    ],
    col_widths=[40, 35, 95]
)

pdf.section_title("3.6 Migration System")
pdf.body_text(
    "Database migrations are handled automatically via a set of _ensure_* functions in db.py. "
    "Each function checks if a column or table exists and creates it if missing. This allows "
    "seamless schema evolution without manual migration scripts."
)

# CHAPTER 4
pdf.chapter_title("API Reference")
pdf.section_title("4.1 API Overview")
pdf.body_text(
    "All API endpoints are prefixed with /api/. The application follows RESTful conventions with "
    "JSON request/response bodies. Authentication is session-based (cookies) with CSRF token protection "
    "on state-changing operations. The API returns appropriate HTTP status codes."
)
pdf.section_title("4.2 Authentication Endpoints")
pdf.add_table(
    ["Method", "Route", "Description"],
    [
        ["GET", "/api/health", "Health check (returns DB engine)"],
        ["POST", "/api/register", "Start registration (sends OTP email)"],
        ["POST", "/api/register/verify", "Verify OTP, create account"],
        ["POST", "/api/register/resend", "Resend registration OTP"],
        ["POST", "/api/login", "Login with username/password"],
        ["POST", "/api/login/totp", "Verify TOTP 2FA code"],
        ["POST", "/api/login/totp/recovery/request", "Request TOTP recovery email"],
        ["POST", "/api/login/totp/recovery/verify", "Verify TOTP recovery code"],
        ["POST", "/api/logout", "Clear session"],
        ["POST", "/api/check-availability", "Check nickname/email availability"],
    ],
    col_widths=[20, 60, 90]
)

pdf.section_title("4.3 User Profile Endpoints")
pdf.add_table(
    ["Method", "Route", "Description"],
    [
        ["GET", "/api/user/me", "Get current user profile"],
        ["POST", "/api/user/totp/setup", "Start TOTP 2FA setup (returns QR)"],
        ["POST", "/api/user/totp/confirm", "Confirm TOTP setup"],
        ["POST", "/api/user/totp/disable", "Disable TOTP 2FA"],
        ["POST", "/api/user/avatar", "Save/clear profile photo"],
        ["POST", "/api/user/ui-preferences", "Save theme/palette preferences"],
        ["POST", "/api/user/profile", "Update personal info"],
        ["POST", "/api/user/profile/email-change-request", "Request email change (OTP)"],
        ["POST", "/api/user/profile/email-change-confirm", "Confirm email change OTP"],
        ["POST", "/api/user/password/change-request", "Request password change (OTP)"],
        ["POST", "/api/user/password/change-confirm", "Confirm password change OTP"],
    ],
    col_widths=[20, 60, 90]
)

pdf.section_title("4.4 Journal Entry Endpoints")
pdf.add_table(
    ["Method", "Route", "Description"],
    [
        ["GET", "/api/entries", "List all user entries"],
        ["POST", "/api/entries", "Create new entry (triggers ML analysis)"],
        ["POST", "/api/entries/analyze-text", "NLP analysis only (no DB write)"],
        ["GET", "/api/entries/<id>", "Get single entry"],
        ["PATCH", "/api/entries/<id>", "Update entry (optional reanalyze)"],
        ["DELETE", "/api/entries/<id>", "Delete entry"],
        ["GET", "/api/tags", "List user tags"],
        ["POST", "/api/tags", "Create tag"],
        ["DELETE", "/api/tags/<tag>", "Delete tag"],
        ["GET", "/api/triggers/summary", "Get stress/happiness trigger analysis"],
    ],
    col_widths=[20, 60, 90]
)

pdf.section_title("4.5 Sync Endpoints")
pdf.add_table(
    ["Method", "Route", "Description"],
    [
        ["GET", "/api/sync/check", "Lightweight sync revision poll"],
        ["GET", "/api/sync/state", "Full sync pull (user + entries)"],
        ["GET", "/api/sync/stream", "SSE stream for live sync"],
    ],
    col_widths=[20, 60, 90]
)

pdf.section_title("4.6 Push Notification Endpoints")
pdf.add_table(
    ["Method", "Route", "Description"],
    [
        ["GET", "/api/push/vapid-public-key", "Get VAPID public key"],
        ["POST", "/api/push/subscribe", "Register push subscription"],
        ["POST", "/api/push/unsubscribe", "Remove push subscription"],
        ["POST", "/api/push/preferences", "Sync notification preferences"],
        ["POST", "/api/push/diagnostics", "Store client push diagnostics"],
        ["GET", "/api/push/schedule-status", "Get push schedule status"],
        ["POST", "/api/push/prune-devices", "Keep only current device"],
        ["POST", "/api/push/reset-daily-reminder", "Clear daily reminder state"],
        ["POST", "/api/push/delivery-ack", "Service worker delivery ack"],
        ["POST", "/api/push/send-daily-test", "Send daily reminder test"],
        ["POST", "/api/push/test", "Send test push notification"],
    ],
    col_widths=[20, 60, 90]
)

pdf.section_title("4.7 Voice & Upload Endpoints")
pdf.add_table(
    ["Method", "Route", "Description"],
    [
        ["POST", "/api/uploads/image", "Upload entry image"],
        ["GET", "/api/voice/status", "Voice transcription status"],
        ["POST", "/api/voice/transcribe", "Server-side voice transcription (Whisper)"],
    ],
    col_widths=[20, 60, 90]
)

pdf.section_title("4.8 Admin Endpoints")
pdf.add_table(
    ["Method", "Route", "Description"],
    [
        ["GET", "/api/admin/dashboard", "Admin dashboard stats"],
        ["GET", "/api/admin/users", "Paginated user list"],
        ["GET", "/api/admin/users/<id>", "User detail view"],
        ["POST", "/api/admin/users/<id>/toggle-status", "Enable/disable user"],
        ["DELETE", "/api/admin/users/<id>", "Delete user account"],
        ["GET", "/api/admin/analytics", "Analytics data"],
        ["GET", "/api/admin/services", "Service health status"],
        ["POST", "/api/admin/services/test-email", "Test Brevo email"],
        ["POST", "/api/admin/services/test-ai", "Test HF Whisper endpoint"],
        ["GET", "/api/admin/audit-logs", "Admin audit logs"],
        ["GET", "/api/admin/settings", "Get system settings"],
        ["POST", "/api/admin/settings", "Save system settings"],
        ["POST", "/api/admin/logout", "Admin logout"],
    ],
    col_widths=[20, 60, 90]
)

# CHAPTER 5
pdf.chapter_title("Authentication & Security")
pdf.section_title("5.1 Registration Flow")
pdf.body_text(
    "User registration follows a two-step OTP-verified process. Step 1: User submits nickname, email, "
    "and password. The system validates inputs, checks availability, generates a 6-digit OTP, and sends "
    "it via Brevo email. A pending_registrations record is created with a 10-minute expiry. Step 2: User "
    "enters the OTP code. If valid, the account is created and the pending registration is deleted."
)
pdf.section_title("5.2 Login Flow")
pdf.body_text(
    "Login authenticates against the users table using werkzeug password hashing. If the user has TOTP "
    "2FA enabled, a login_totp_challenges record is created and the user is redirected to the TOTP verification "
    "page. The challenge token expires after 5 minutes. On successful 2FA verification, the session is established."
)
pdf.section_title("5.3 Two-Factor Authentication (TOTP)")
pdf.body_text(
    "TOTP 2FA uses pyotp library compatible with Google Authenticator. Setup flow: 1) User enters password to "
    "confirm identity. 2) System generates a TOTP secret and displays a QR code (via segno). 3) User scans QR "
    "with authenticator app and enters 6-digit code to confirm. The secret is stored in the users table. "
    "Recovery: Users can request a TOTP recovery email with a one-time code if they lose access to their "
    "authenticator app. The recovery code is valid for 15 minutes."
)
pdf.section_title("5.4 Password Policy")
pdf.body_text("Enforced rules (validated in password_policy.py):")
pdf.bullet_list([
    "Length: 12-64 characters",
    "Must contain: uppercase letter, lowercase letter, digit, special character",
    "No spaces allowed",
    "Cannot be in common passwords list (14 entries)",
    "Cannot contain username, email, first name, or last name",
    "Special characters limited to: !@#$%^&*()_+-=[]{}|;:,.<>?",
])
pdf.section_title("5.5 Login Lockout System")
pdf.body_text(
    "Implemented in auth_security.py with an in-memory sliding window rate limiter. After 5 failed login "
    "attempts, the account is locked for 15 minutes (900 seconds). Lockout is tracked by account_key "
    "(derived from the login identifier). On successful login, all lockout state is cleared."
)
pdf.section_title("5.6 OTP Rate Limiting")
pdf.body_text(
    "OTP requests are rate-limited to 5 per 15-minute window per flow. This applies to: registration resend, "
    "login recovery, email change, password change, and password forgot flows. After 5 requests, the user "
    "must wait 15 minutes before trying again. Limits are stored in 5 separate database tables."
)
pdf.section_title("5.7 CSRF Protection")
pdf.body_text(
    "Cross-Site Request Forgery protection is implemented via X-CSRF-Token header validation. On login, "
    "a CSRF token is generated and stored in the session. All state-changing requests (POST, PATCH, DELETE) "
    "must include this token in the X-CSRF-Token header. Additionally, Origin and Referer headers are validated."
)
pdf.section_title("5.8 Password Reset")
pdf.body_text(
    "Users can request a password reset via the forgot password flow. A 6-digit OTP is generated and sent "
    "via Brevo email. The code expires in 15 minutes. After verification, the user can set a new password. "
    "The reset code is deleted after successful password change."
)
pdf.section_title("5.9 Email Change with OTP")
pdf.body_text(
    "Email changes require OTP verification. When a user requests an email change, a 6-digit OTP is sent "
    "to the new email address. After verification, the email is updated. This prevents account takeover "
    "if the current session is compromised."
)
pdf.section_title("5.10 Content Security Policy (CSP)")
pdf.body_text(
    "The application sends a strict Content-Security-Policy header that restricts script sources, "
    "style sources, image sources, and connection origins. CSP can be disabled via DIARI_DISABLE_CSP=1 "
    "for debugging purposes. The policy includes directives for Hugging Face, Brevo, and WebSocket connections."
)
pdf.section_title("5.11 Input Security")
pdf.body_text(
    "All user inputs are sanitized in input_security.py. Angle brackets are rejected to prevent XSS. "
    "Null bytes are stripped. Nicknames are validated for length (4-64 chars). Emails are validated for "
    "format. Tags are validated via regex. Entry text is normalized. Image URLs must use /uploads/ paths. "
    "Entry titles are limited to 180 characters."
)

# CHAPTER 6
pdf.chapter_title("Machine Learning Pipeline")
pdf.section_title("6.1 Overview")
pdf.body_text(
    "The ML pipeline provides emotion classification and sentiment analysis for journal entries. "
    "Instead of running the model on the web server (which would exceed free-tier RAM limits), "
    "the inference is offloaded to a Hugging Face Space. This keeps the Flask app lightweight "
    "while providing high-quality NLP analysis."
)
pdf.section_title("6.2 Model Architecture")
pdf.add_table(
    ["Property", "Value"],
    [
        ["Base Model", "XLM-RoBERTa-base (xlm-roberta-base)"],
        ["Task", "Multi-class emotion classification (5 classes)"],
        ["Classes", "angry, anxious, happy, neutral, sad"],
        ["Training Framework", "Google Colab (PyTorch)"],
        ["Export Format", "ONNX (Open Neural Network Exchange)"],
        ["Model Size", "~1 GB (ONNX)"],
        ["Tokenizer", "XLM-RoBERTa tokenizer (SentencePiece)"],
        ["Sentiment Mapping", "happy->positive, sad/angry/anxious->negative, neutral->neutral"],
    ],
    col_widths=[50, 120]
)

pdf.section_title("6.3 Training Details")
pdf.body_text("The model was trained in Google Colab using the DiariCore_Model_Final_Cleaned.ipynb notebook.")
pdf.bullet_list([
    "Base model: xlm-roberta-base (multilingual, supports English, Filipino, Taglish)",
    "Loss function: FocalLoss with Label Smoothing (alpha=0.25, gamma=2.0, smoothing=0.1)",
    "Optimizer: AdamW with differential learning rates (2e-5 for base, 1e-4 for classifier head)",
    "Learning rate scheduler: Linear warmup (10% steps) then cosine decay",
    "Regularization: Stochastic Weight Averaging (SWA), weight decay=0.01",
    "Data augmentation: synonym replacement, back-translation, random swap, random deletion",
    "Training: 3 epochs, batch size 8, max sequence length 128",
    "Class weights: inverse frequency weighting to handle class imbalance",
    "Hardware: Google Colab GPU (T4)",
])

pdf.section_title("6.4 Dataset")
pdf.body_text(
    "The training dataset is a custom collection of 1,593 labeled journal entries across three languages. "
    "It was expanded from an initial 1,500 samples through data augmentation techniques."
)
pdf.add_table(
    ["Property", "Value"],
    [
        ["Total Records", "1,593"],
        ["Columns", "text, label, language"],
        ["Emotion Classes", "angry (319), anxious (319), happy (319), neutral (318), sad (318)"],
        ["Languages", "English, Filipino, Taglish (code-switched)"],
        ["Data Source", "Custom journal entries with manual annotation"],
        ["File", "1500_dataset_expanded.xlsx"],
        ["Balance", "Approximately balanced across 5 classes"],
    ],
    col_widths=[50, 120]
)

pdf.section_title("6.5 Inference Architecture")
pdf.body_text(
    "The Hugging Face Space (sseia/diaricore-inference) runs a FastAPI application that loads the ONNX "
    "model and exposes a /predict endpoint. The Flask backend (space_nlp.py) sends HTTP POST requests "
    "to this endpoint. The Space handles tokenization, inference, and probability computation."
)
pdf.code_block(
    "Flask App --> space_nlp.analyze(text)\n"
    "    --> POST https://sseia-diaricore-inference.hf.space/predict\n"
    "        --> { text: '...' }\n"
    "    <-- {\n"
    "        sentimentLabel: 'positive',\n"
    "        sentimentScore: 0.92,\n"
    "        emotionLabel: 'happy',\n"
    "        emotionScore: 0.87,\n"
    "        all_probs: { happy: 0.87, sad: 0.03, ... },\n"
    "        engine: 'hf-custom'\n"
    "    }"
)

pdf.section_title("6.6 Fallback Mechanism")
pdf.body_text(
    "When the Hugging Face Space is unreachable (cold start, network error, or timeout), "
    "space_nlp.py falls back to a keyword-based heuristic. This uses simple keyword matching "
    "for common emotion words (e.g., 'happy', 'sad', 'worried', 'angry') to provide basic "
    "analysis. The fallback is less accurate but keeps the app responsive."
)
pdf.section_title("6.7 Voice Transcription")
pdf.body_text(
    "Voice transcription uses OpenAI Whisper (openai/whisper-large-v3-turbo) via Hugging Face Inference API. "
    "The flow: 1) Browser records audio. 2) Audio blob is sent to /api/voice/transcribe. 3) Server POSTs "
    "to HF Inference API with the audio file. 4) Transcribed text is returned. The system has a 25-second "
    "timeout with retry on 503 errors. Falls back to InferenceClient if direct HTTP fails."
)

# CHAPTER 7
pdf.chapter_title("Progressive Web App (PWA)")
pdf.section_title("7.1 PWA Configuration")
pdf.body_text(
    "DiariCore implements a full PWA with offline support, installability, and push notifications. "
    "The manifest defines the app as standalone with portrait orientation, targeting lifestyle and health categories."
)
pdf.add_table(
    ["Property", "Value"],
    [
        ["Name", "DiariCore"],
        ["Short Name", "DiariCore"],
        ["Display", "standalone"],
        ["Orientation", "portrait-primary"],
        ["Start URL", "/dashboard.html"],
        ["Scope", "/"],
        ["Theme Color", "#ffffff"],
        ["Background Color", "#ffffff"],
        ["Categories", "lifestyle, health"],
        ["Icons", "192x192 (any), 512x512 (any), 512x512 (maskable)"],
        ["Shortcuts", "Write entry (/write-entry.html), Dashboard (/dashboard.html)"],
    ],
    col_widths=[45, 125]
)

pdf.section_title("7.2 Service Worker")
pdf.body_text(
    "The service worker (static/service-worker.js) manages offline caching, push notifications, "
    "and notification click handling. It uses a versioned cache (v139) and implements different "
    "strategies for different resource types."
)
pdf.add_table(
    ["Resource Type", "Strategy", "Description"],
    [
        ["Navigation", "Cache-first, network fallback", "Offline shell with /dashboard.html fallback"],
        ["JS/CSS", "Stale-while-revalidate", "Serve cached, update in background"],
        ["Images/Fonts", "Cache-first", "Cache on first load, serve from cache"],
        ["API routes", "Network only", "Never cache dynamic API responses"],
        ["HTML pages", "Precache", "81 URLs precached on install"],
    ],
    col_widths=[40, 50, 80]
)

pdf.section_title("7.3 PWA Launch Animation")
pdf.body_text(
    "When the PWA is launched in standalone mode, a multi-stage animation plays: 1) White screen "
    "splash. 2) Loading bar Lottie animation. 3) Explosion Lottie animation with brand reveal "
    "at 38% progress. 4) Brand hold for 2.5 seconds. 5) App reveal. The animation is skipped "
    "on fast-open (notification click), auth pages, and after first launch in a session."
)
pdf.section_title("7.4 Theme System")
pdf.body_text(
    "The PWA supports 10 color palettes (theme-1 through theme-10) and light/dark modes. "
    "pwa-theme-early.js applies the palette BEFORE stylesheets paint to prevent flash of wrong color. "
    "It reads preferences from localStorage and sets 13+ CSS custom properties on :root. "
    "The manifest theme_color is #ffffff to prevent Android status bar coloring during splash."
)
pdf.section_title("7.5 Offline Support")
pdf.body_text(
    "The PWA provides offline access to the dashboard and previously cached pages. The service worker "
    "serves precached shell assets when offline. Entry data is stored in localStorage for offline "
    "reading. The diari-offline.js module manages offline state detection and sync queue."
)
pdf.section_title("7.6 Cross-Device Sync")
pdf.body_text(
    "DiariCore supports real-time cross-device synchronization via Server-Sent Events (SSE). "
    "The /api/sync/stream endpoint provides an SSE connection. When entries change on any device, "
    "the server pushes a sync event to all connected clients. The sync system uses SHA256-based "
    "revision tracking for efficient change detection."
)

# CHAPTER 8
pdf.chapter_title("Push Notification System")
pdf.section_title("8.1 Notification Architecture")
pdf.body_text(
    "Push notifications are delivered via Web Push (VAPID/FCM). The system supports three types of "
    "notifications: daily journaling reminders, streak reminders, and insight follow-ups. "
    "The push scheduler runs as a background daemon thread in the Gunicorn worker process."
)
pdf.section_title("8.2 Notification Types & Schedules")
pdf.add_table(
    ["Type", "Schedule", "Content", "Template Count"],
    [
        ["Daily Reminder", "User-configurable time (default 9 AM Manila)", "Gentle journaling nudge", "30 templates"],
        ["Streak 1-Hour", "9 PM Manila (if streak at risk)", "Streak warning (1 hour left)", "30 templates"],
        ["Streak 30-Min", "11 PM Manila (if streak at risk)", "Last chance (30 min left)", "30 templates"],
        ["Insight Follow-up", "45min-36h after entry", "Reflective insight on last entry", "100 combinations"],
    ],
    col_widths=[35, 50, 50, 35]
)

pdf.section_title("8.3 Notification Phrase Randomization")
pdf.body_text(
    "Each notification type uses randomly selected phrases to keep notifications fresh and engaging. "
    "Server-side uses random.choice(), client-side uses Math.random(). Templates are defined in "
    "push-templates.json (canonical source) and pwa-notification-templates.js (client mirror)."
)
pdf.bullet_list([
    "Daily reminders: 30 unique gentle phrases (e.g., 'A gentle check-in with yourself might feel good.')",
    "Streak reminders: 30 unique streak-themed phrases with {streak} placeholder",
    "Insight follow-ups: 5 mood buckets x 5 templates x 4 phrase slots = 100 unique combinations",
    "Mood buckets: high (happy), low (sad/anxious/angry), neutral, mid (fallback)",
    "Each insight includes: tone description, insight content, entry title, and reflective phrase",
])
pdf.section_title("8.4 Push Delivery Flow")
pdf.code_block(
    "1. push_scheduler.py daemon thread (60s interval)\n"
    "2. --> dispatch_due_notifications() in push_service.py\n"
    "3.     --> Check daily reminders (Manila timezone)\n"
    "4.     --> Check streak reminders (9PM, 11PM)\n"
    "5.     --> Check insight follow-ups (45min-36h after entry)\n"
    "6.     --> Build notification with random phrase\n"
    "7.     --> Send via pywebpush (VAPID signed)\n"
    "8.     --> Service Worker receives push event\n"
    "9.     --> Shows notification with icon/badge/vibrate\n"
    "10.    --> User taps --> Opens dashboard.html?pwa_fast=1"
)

pdf.section_title("8.5 Subscription Management")
pdf.body_text(
    "Users can have multiple push subscriptions (one per device/browser). The system tracks FCM "
    "delivery failures per subscription. After 3 consecutive failures, the subscription is purged. "
    "Users can prune devices to keep only the current device. Subscriptions are verified against "
    "the current VAPID key to detect stale subscriptions from key rotation."
)
pdf.section_title("8.6 Notification Click Handling")
pdf.body_text(
    "When a notification is clicked, the service worker builds an absolute URL with ?pwa_fast=1 "
    "parameter. It tries to focus an existing client window first, then opens a new window if needed. "
    "The URL always points to /dashboard.html regardless of notification type. The pwa_fast=1 parameter "
    "skips the splash animation for instant feedback."
)

# CHAPTER 9
pdf.chapter_title("Frontend Pages & Templates")
pdf.section_title("9.1 Page Overview")
pdf.body_text("DiariCore has 14 HTML templates, each serving a specific purpose in the application flow.")
pdf.add_table(
    ["Template", "Purpose", "Key Scripts"],
    [
        ["login.html", "User login page", "login.js, pwa-auth-bootstrap.js, theme.js"],
        ["register.html", "User registration with privacy consent", "register.js, password-live.js, theme.js"],
        ["verify-registration.html", "OTP verification after registration", "verify-registration.js"],
        ["dashboard.html", "Main dashboard (PWA start_url)", "dashboard.js, chart-flow.js, pwa.js"],
        ["write-entry.html", "Journal entry editor", "write-entry.js, image-upload-utils.js"],
        ["voice-entry.html", "Voice journal entry", "voice-entry.js, voice-transcribe-client.js"],
        ["entries.html", "Entry list with search/filter", "entries.js, side-bar.js"],
        ["entry-view.html", "Single entry detail view", "entry-view.js, mood-analysis-ui.js"],
        ["insights.html", "Analytics and insights charts", "insights.js, chart-flow.js"],
        ["suggestions.html", "Smart suggestions page", "suggestions.js"],
        ["profile.html", "User profile and settings", "profile.js (3,355 lines)"],
        ["admin.html", "Admin dashboard", "admin.js"],
        ["side-bar.html", "Sidebar navigation component", "side-bar.js"],
        ["pwa-splash.html", "PWA splash screen overlay", "pwa-splash-boot.js"],
    ],
    col_widths=[40, 55, 75]
)

pdf.section_title("9.2 Page Descriptions")
pdf.subsection_title("Login & Registration")
pdf.body_text(
    "login.html: Login page with username/password fields, 'Forgot Password' link, and 'Create Account' "
    "link. Supports PWA fast-open from notifications. register.html: Registration form with first/last "
    "name, nickname, email, password (with live strength indicator), birthday, gender, and privacy "
    "consent checkbox. verify-registration.html: OTP verification page after registration with 6-digit "
    "input fields and resend option."
)
pdf.subsection_title("Dashboard")
pdf.body_text(
    "dashboard.html: Main page after login. Shows quick stats (entries count, streak, mood distribution), "
    "recent entries preview, weekly mood chart, and quick-write button. This is the PWA start_url and "
    "the target of all notification clicks. Loads the most JavaScript modules including PWA bootstrap."
)
pdf.subsection_title("Entry Management")
pdf.body_text(
    "write-entry.html: Full entry editor with title, rich text area, tag selector, image upload, "
    "date/time picker, and Save & Analyze button. voice-entry.html: Voice recording interface with "
    "real-time waveform visualization, recording controls, and automatic transcription. entries.html: "
    "Searchable and filterable entry list with sidebar tag navigation, date range filter, and clear/apply buttons. "
    "entry-view.html: Single entry detail with mood analysis visualization, tag display, and edit/delete actions."
)
pdf.subsection_title("Analytics & Insights")
pdf.body_text(
    "insights.html: Comprehensive analytics with Chart.js charts showing mood trends, emotion distribution, "
    "tag correlations, and journaling consistency. suggestions.html: Smart suggestions page with activity "
    "recommendations and supportive messages based on recent emotional patterns."
)
pdf.subsection_title("Profile & Admin")
pdf.body_text(
    "profile.html: User profile with sections for personal info editing, avatar upload, password change "
    "(OTP-verified), email change (OTP-verified), 2FA setup/disable, notification preferences, and "
    "reminder time configuration. admin.html: Admin dashboard with user management, analytics, "
    "service health monitoring, system settings, and audit logs."
)

# CHAPTER 10
pdf.chapter_title("Frontend JavaScript Modules")
pdf.section_title("10.1 Module Overview")
pdf.body_text("DiariCore has 39 JavaScript modules under static/js/. Here are the key modules:")
pdf.add_table(
    ["Module", "Lines", "Purpose"],
    [
        ["pwa.js", "577", "Core PWA bootstrap: manifest, SW registration, install banner"],
        ["pwa-theme-early.js", "238", "Early theme application to prevent flash of wrong color"],
        ["diari-pwa-launch.js", "376", "PWA-only animated launch screen (Lottie)"],
        ["pwa-web-push.js", "927", "VAPID/FCM push subscription management"],
        ["pwa-notifications.js", "485", "Client-side notification manager, IDB sync"],
        ["pwa-notification-scheduler-sw.js", "283", "Service worker notification scheduling"],
        ["pwa-notification-templates.js", "249", "Notification phrase templates (client mirror)"],
        ["profile.js", "3,355", "Complete profile page logic"],
        ["dashboard.js", "N/A", "Dashboard page initialization"],
        ["write-entry.js", "N/A", "Entry editor with ML analysis"],
        ["entries.js", "N/A", "Entry list with search/filter"],
        ["entry-view.js", "N/A", "Single entry detail view"],
        ["insights.js", "N/A", "Analytics charts and insights"],
        ["diari-offline.js", "N/A", "Offline state management and sync"],
        ["diari-security.js", "N/A", "CSRF token handling, secure fetch"],
        ["diari-streak.js", "N/A", "Journaling streak computation"],
        ["chart-flow.js", "N/A", "Chart.js chart initialization"],
        ["mood-analysis-ui.js", "N/A", "Mood visualization components"],
        ["theme.js", "N/A", "Theme/palette switching logic"],
        ["side-bar.js", "N/A", "Sidebar navigation component"],
    ],
    col_widths=[45, 20, 105]
)

pdf.section_title("10.2 Key Module Details")
pdf.subsection_title("pwa.js - Core Bootstrap")
pdf.body_text(
    "Manages the complete PWA lifecycle: injects manifest and meta tags into <head>, registers the "
    "service worker, handles the install prompt (beforeinstallprompt), creates the install banner, "
    "and coordinates with other PWA modules. Loads the notification script stack sequentially. "
    "Provides the global DiariPWA API."
)
pdf.subsection_title("pwa-web-push.js - Push Registration")
pdf.body_text(
    "Handles the complete push notification lifecycle: validates PWA context, checks notification "
    "permission, fetches VAPID public key, creates PushManager subscription, saves to server, "
    "and runs diagnostics. Includes retry logic (6 attempts), watchdog timer, and stale subscription "
    "detection. Provides the global DiariPwaWebPush API."
)
pdf.subsection_title("diari-offline.js - Offline Support")
pdf.body_text(
    "Manages offline state detection, offline entry queue, and sync operations. When the browser "
    "goes offline, entries are saved locally. When connectivity returns, pending entries are synced "
    "to the server. Handles avatar sync, tag sync, and entry sync with conflict resolution."
)
pdf.subsection_title("profile.js - Profile Management")
pdf.body_text(
    "The largest JS module at 3,355 lines. Handles: personal info editing with live validation, "
    "avatar upload with client-side resize (360px max, JPEG 0.86 quality), password change with "
    "OTP verification and auto-logout, email change with OTP, TOTP 2FA setup/disable with QR code "
    "display, notification preference toggles, reminder time configuration, and section navigation."
)

# CHAPTER 11
pdf.chapter_title("Frontend CSS & Theming")
pdf.section_title("11.1 CSS File Overview")
pdf.add_table(
    ["File", "Purpose"],
    [
        ["theme.css", "Core theme variables, color palettes, dark mode"],
        ["mobile-global.css", "Global mobile overrides, overflow-x: clip"],
        ["diari-shell-pending.css", "Shell loading state styles"],
        ["diari-pwa-launch.css", "PWA launch animation overlay styles"],
        ["pwa.css", "PWA install banner, notification controls"],
        ["login.css", "Login page styles"],
        ["register.css", "Registration page styles"],
        ["verify-registration.css", "OTP verification page styles"],
        ["password-live.css", "Password strength indicator"],
        ["dashboard.css", "Dashboard layout and components"],
        ["side-bar.css", "Sidebar navigation styles"],
        ["entries.css", "Entry list and filter styles"],
        ["entry-view.css", "Entry detail view styles"],
        ["write-entry.css", "Entry editor styles"],
        ["voice-entry.css", "Voice recording interface styles"],
        ["chart-flow.css", "Chart.js chart container styles"],
        ["insights.css", "Analytics page styles"],
        ["suggestions.css", "Smart suggestions styles"],
        ["profile.css", "Profile page styles"],
        ["admin.css", "Admin dashboard styles"],
        ["vendor/bootstrap-icons.css", "Bootstrap Icons library"],
    ],
    col_widths=[55, 115]
)

pdf.section_title("11.2 Theme System")
pdf.body_text(
    "The theming system supports 10 color palettes and light/dark modes. Each palette defines a "
    "primary color that generates derived colors (hover, light, accent, tints) via CSS functions "
    "and JavaScript calculations. The theme.css file defines CSS custom properties that all other "
    "stylesheets reference."
)
pdf.add_table(
    ["Palette", "Primary Color", "Description"],
    [
        ["theme-1", "#6F8F7F", "Sage Green (default)"],
        ["theme-2", "#8E7CB5", "Soft Purple"],
        ["theme-3", "#6F9BB8", "Steel Blue"],
        ["theme-4", "#D89A82", "Warm Coral"],
        ["theme-5", "#4FAFB0", "Teal"],
        ["theme-6", "#B5957E", "Warm Taupe"],
        ["theme-7", "#BC7E97", "Dusty Rose"],
        ["theme-8", "#6FAF9B", "Mint Green"],
        ["theme-9", "#A97B95", "Mauve"],
        ["theme-10", "#7F9393", "Slate Teal"],
    ],
    col_widths=[30, 40, 100]
)

pdf.section_title("11.3 Mobile Responsiveness")
pdf.body_text(
    "mobile-global.css applies critical mobile overrides. overflow-x: clip is set on <html>, which "
    "per CSS spec forces overflow-y to auto, making <html> the actual scroll root on mobile. "
    "This prevents horizontal scroll issues. The PWA install banner uses full-width buttons with "
    "a separator line on mobile for better touch targets."
)

# CHAPTER 12
pdf.chapter_title("Deployment & Infrastructure")
pdf.section_title("12.1 Deployment Platforms")
pdf.add_table(
    ["Platform", "URL", "Purpose"],
    [
        ["Railway", "diaricore.up.railway.app", "Primary production deployment"],
        ["AWS EC2", "16.176.11.240", "Secondary/self-managed deployment"],
        ["Hugging Face Spaces", "sseia/diaricore-inference", "ML inference service"],
        ["Hugging Face Hub", "sseia/diari-core-mood", "ML model storage"],
    ],
    col_widths=[45, 55, 70]
)

pdf.section_title("12.2 Railway Deployment")
pdf.body_text(
    "Railway is the primary deployment platform. The app runs via Gunicorn with the Procfile: "
    "'web: gunicorn app:app -c gunicorn.conf.py'. Environment variables are configured in the "
    "Railway dashboard. A PostgreSQL plugin provides the production database. Railway auto-deploys "
    "on push to the master branch."
)
pdf.section_title("12.3 Gunicorn Configuration")
pdf.add_table(
    ["Setting", "Value", "Description"],
    [
        ["bind", "0.0.0.0:$PORT", "Listens on Railway-assigned port"],
        ["workers", "WEB_CONCURRENCY (default 1)", "Number of worker processes"],
        ["threads", "1", "Threads per worker"],
        ["timeout", "120", "Request timeout in seconds"],
        ["post_fork", "push_scheduler.start()", "Starts push daemon in each worker"],
    ],
    col_widths=[40, 55, 75]
)

pdf.section_title("12.4 AWS EC2 Deployment")
pdf.body_text(
    "The secondary deployment runs on an AWS EC2 instance (16.176.11.240). Setup requires: Python 3, "
    "PostgreSQL, Nginx reverse proxy, systemd service management. Environment variables include "
    "DATABASE_URL, SECRET_KEY, UPLOADS_DIR, and Brevo keys."
)
pdf.section_title("12.5 Hugging Face Space")
pdf.body_text(
    "The ML inference service runs as a Hugging Face Space with a Docker-based deployment. "
    "The Dockerfile installs Python dependencies and runs the FastAPI app. The space loads "
    "the ONNX model from the Hugging Face Hub on startup. It exposes a /predict endpoint "
    "that accepts text and returns emotion/sentiment analysis."
)

# CHAPTER 13
pdf.chapter_title("Configuration & Environment Variables")
pdf.section_title("13.1 Environment Variables")
pdf.add_table(
    ["Variable", "Required", "Default", "Description"],
    [
        ["SECRET_KEY", "Yes (prod)", "None", "Flask session signing key (32+ chars)"],
        ["DATABASE_URL", "No", "None (uses SQLite)", "PostgreSQL connection string"],
        ["DATABASE_PATH", "No", "diaricore.db", "SQLite file path"],
        ["SPACE_URL", "No", "https://sseia-diaricore-inference.hf.space", "HF Space inference URL"],
        ["DIARI_ADMIN_EMAIL", "No", "None", "Admin account email"],
        ["DIARI_DISABLE_CSP", "No", "0", "Disable CSP (debug only)"],
        ["BREVO_API_KEY", "No", "None", "Brevo email API key"],
        ["BREVO_SENDER_EMAIL", "No", "None", "Brevo sender email"],
        ["BREVO_SENDER_NAME", "No", "DiariCore", "Brevo sender name"],
        ["HF_TOKEN", "No", "None", "HuggingFace API token (voice)"],
        ["HF_SPEECH_MODEL", "No", "openai/whisper-large-v3", "Voice model ID"],
        ["WEB_CONCURRENCY", "No", "1", "Gunicorn worker count"],
        ["DISABLE_INTERNAL_PUSH_CRON", "No", "0", "Disable push scheduler"],
    ],
    col_widths=[45, 20, 45, 60]
)

pdf.section_title("13.2 Python Dependencies")
pdf.add_table(
    ["Package", "Version", "Purpose"],
    [
        ["flask", ">=3.0.0", "Web framework"],
        ["gunicorn", ">=21.0.0", "WSGI server"],
        ["psycopg2-binary", ">=2.9.9", "PostgreSQL driver"],
        ["httpx", ">=0.28.0", "Async HTTP client (HF Space calls)"],
        ["huggingface_hub", ">=0.28.0", "HF model hub access"],
        ["pyotp", ">=2.9.0", "TOTP 2FA"],
        ["segno", ">=1.6.0", "QR code generation"],
        ["pywebpush", ">=2.0.0", "Web Push (VAPID/FCM)"],
        ["py-vapid", ">=1.9.0", "VAPID key generation"],
        ["cryptography", ">=42.0.0", "Crypto operations"],
    ],
    col_widths=[40, 30, 100]
)

# APPENDIX A
pdf.chapter_title("Complete API Endpoint Reference")
pdf.section_title("A.1 All Endpoints Summary")
pdf.body_text("Complete listing of all 45+ API endpoints organized by module.")
pdf.add_table(
    ["#", "Method", "Route", "Auth", "Description"],
    [
        ["1", "GET", "/api/health", "No", "Health check"],
        ["2", "POST", "/api/register", "No", "Start registration (OTP)"],
        ["3", "POST", "/api/register/verify", "No", "Verify OTP, create account"],
        ["4", "POST", "/api/register/resend", "No", "Resend registration OTP"],
        ["5", "POST", "/api/login", "No", "Login with credentials"],
        ["6", "POST", "/api/login/totp", "Challenge", "Verify TOTP 2FA"],
        ["7", "POST", "/api/login/totp/recovery/request", "Challenge", "Request TOTP recovery"],
        ["8", "POST", "/api/login/totp/recovery/verify", "Challenge", "Verify recovery code"],
        ["9", "POST", "/api/logout", "Yes", "Clear session"],
        ["10", "GET", "/api/user/me", "Yes", "Get current user"],
        ["11", "POST", "/api/user/totp/setup", "Yes", "Start TOTP setup"],
        ["12", "POST", "/api/user/totp/confirm", "Yes", "Confirm TOTP setup"],
        ["13", "POST", "/api/user/totp/disable", "Yes", "Disable TOTP"],
        ["14", "POST", "/api/user/avatar", "Yes", "Save avatar"],
        ["15", "POST", "/api/user/ui-preferences", "Yes", "Save UI preferences"],
        ["16", "POST", "/api/user/profile", "Yes", "Update profile"],
        ["17", "POST", "/api/user/profile/email-change-request", "Yes", "Request email change"],
        ["18", "POST", "/api/user/profile/email-change-confirm", "Yes", "Confirm email change"],
        ["19", "POST", "/api/user/password/change-request", "Yes", "Request password change"],
        ["20", "POST", "/api/user/password/change-confirm", "Yes", "Confirm password change"],
        ["21", "POST", "/api/password/forgot", "No", "Request password reset"],
        ["22", "POST", "/api/password/reset", "No", "Reset password"],
        ["23", "POST", "/api/password/verify-code", "No", "Verify reset code"],
        ["24", "GET", "/api/sync/check", "Yes", "Sync revision poll"],
        ["25", "GET", "/api/sync/state", "Yes", "Full sync pull"],
        ["26", "GET", "/api/sync/stream", "Yes", "SSE live sync"],
        ["27", "GET", "/api/entries", "Yes", "List entries"],
        ["28", "POST", "/api/entries", "Yes", "Create entry"],
        ["29", "POST", "/api/entries/analyze-text", "Yes", "NLP analysis only"],
        ["30", "GET", "/api/entries/<id>", "Yes", "Get entry"],
        ["31", "PATCH", "/api/entries/<id>", "Yes", "Update entry"],
        ["32", "DELETE", "/api/entries/<id>", "Yes", "Delete entry"],
        ["33", "GET", "/api/tags", "Yes", "List tags"],
        ["34", "POST", "/api/tags", "Yes", "Create tag"],
        ["35", "DELETE", "/api/tags/<tag>", "Yes", "Delete tag"],
        ["36", "GET", "/api/triggers/summary", "Yes", "Trigger analysis"],
        ["37", "POST", "/api/uploads/image", "Yes", "Upload image"],
        ["38", "GET", "/api/voice/status", "Yes", "Voice status"],
        ["39", "POST", "/api/voice/transcribe", "Yes", "Voice transcription"],
        ["40", "GET", "/api/push/vapid-public-key", "Yes", "VAPID public key"],
        ["41", "POST", "/api/push/subscribe", "Yes", "Register subscription"],
        ["42", "POST", "/api/push/unsubscribe", "Yes", "Remove subscription"],
        ["43", "POST", "/api/push/preferences", "Yes", "Sync notification prefs"],
        ["44", "GET", "/api/push/schedule-status", "Yes", "Push schedule status"],
        ["45", "POST", "/api/push/test", "Yes", "Send test push"],
        ["46", "POST", "/api/check-availability", "No", "Check nickname/email"],
        ["47", "POST", "/api/admin/*", "Admin", "Admin endpoints (13 routes)"],
    ],
    col_widths=[8, 16, 60, 16, 70]
)

# APPENDIX B
pdf.chapter_title("Database Table Definitions")
pdf.section_title("B.1 Table Creation SQL")
pdf.body_text(
    "The following SQL represents the PostgreSQL table definitions used by DiariCore. "
    "The actual code uses db.py init_db() which handles both PostgreSQL and SQLite."
)

pdf.subsection_title("users")
pdf.code_block(
    "CREATE TABLE users (\n"
    "    id            SERIAL PRIMARY KEY,\n"
    "    nickname      VARCHAR(64) UNIQUE NOT NULL,\n"
    "    email         VARCHAR(254) UNIQUE NOT NULL,\n"
    "    password_hash TEXT NOT NULL,\n"
    "    first_name    VARCHAR(64),\n"
    "    last_name     VARCHAR(64),\n"
    "    gender        VARCHAR(20),\n"
    "    birthday      DATE,\n"
    "    avatar_data_url TEXT,\n"
    "    ui_preferences_json JSONB DEFAULT '{}',\n"
    "    totp_secret   TEXT,\n"
    "    totp_enabled  BOOLEAN DEFAULT FALSE,\n"
    "    totp_setup_secret TEXT,\n"
    "    totp_setup_expires TIMESTAMP,\n"
    "    is_disabled   BOOLEAN DEFAULT FALSE,\n"
    "    privacy_agreed_at TIMESTAMP,\n"
    "    last_login    TIMESTAMP,\n"
    "    created_at    TIMESTAMP DEFAULT NOW()\n"
    ");"
)

pdf.subsection_title("journal_entries")
pdf.code_block(
    "CREATE TABLE journal_entries (\n"
    "    id                 SERIAL PRIMARY KEY,\n"
    "    user_id            INTEGER REFERENCES users(id) ON DELETE CASCADE,\n"
    "    title              VARCHAR(180),\n"
    "    entry_datetime_utc TIMESTAMP,\n"
    "    text_content       TEXT NOT NULL,\n"
    "    tags_json          JSONB DEFAULT '[]',\n"
    "    sentiment          VARCHAR(12),\n"
    "    emotion            VARCHAR(12),\n"
    "    all_probs_json     JSONB DEFAULT '{}',\n"
    "    image_urls_json    JSONB DEFAULT '[]',\n"
    "    created_at         TIMESTAMP DEFAULT NOW(),\n"
    "    updated_at         TIMESTAMP\n"
    ");"
)

pdf.subsection_title("push_subscriptions")
pdf.code_block(
    "CREATE TABLE push_subscriptions (\n"
    "    id                SERIAL PRIMARY KEY,\n"
    "    user_id           INTEGER REFERENCES users(id) ON DELETE CASCADE,\n"
    "    endpoint          TEXT UNIQUE NOT NULL,\n"
    "    subscription_json JSONB NOT NULL,\n"
    "    created_at        TIMESTAMP DEFAULT NOW(),\n"
    "    fcm_failures      INTEGER DEFAULT 0\n"
    ");"
)

pdf.subsection_title("login_lockouts")
pdf.code_block(
    "CREATE TABLE login_lockouts (\n"
    "    account_key  VARCHAR(255) PRIMARY KEY,\n"
    "    attempts_json JSONB DEFAULT '[]',\n"
    "    locked_until TIMESTAMP\n"
    ");"
)

pdf.section_title("B.2 Indexes")
pdf.body_text(
    "Key indexes for performance:"
)
pdf.bullet_list([
    "journal_entries(user_id) - Entry lookup by user",
    "journal_entries(created_at) - Chronological sorting",
    "push_subscriptions(user_id) - Push lookup by user",
    "push_subscriptions(endpoint) - Unique endpoint constraint",
    "users(nickname) - Login lookup",
    "users(email) - Login and uniqueness check",
    "admin_audit_logs(admin_email) - Audit log filtering",
])

pdf.section_title("B.3 Document Version")
pdf.body_text(
    "This documentation was generated in August 2026 based on the DiariCore codebase at commit level "
    "reflecting the latest features including PWA push notifications, TOTP 2FA, offline support, "
    "voice transcription, and admin tools."
)

output_path = os.path.join(os.path.dirname(__file__), "DiariCore_System_Documentation.pdf")
pdf.output(output_path)
print(f"PDF generated: {output_path}")
