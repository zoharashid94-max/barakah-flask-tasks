# Full-Stack Python Web Application (Flask Framework Portfolio)

A fully functional, database-backed web application engineered during my backend development internship at **Barakah TechLabs**. This project showcases the implementation of production-grade architecture, ranging from dynamic routing to secure relational database storage and RESTful APIs.

---

## Key Milestones Achieved

The application successfully integrates 5 distinct development architectural blocks:

*   **Task 1: Flask Infrastructure & Jinja2 Engineering** – Established dynamic backend routing, handled clean status rendering, and implemented structured template inheritance using a master base layout.
*   **Task 2: Server-Side Form Handling & Request Parsing** – Engineered an input interface optimized to handle server-side HTTP `POST` requests, safely parsing client-side inputs.
*   **Task 3: Relational SQLite Database Integration** – Automated transactional schema execution to dynamically insert, persist, and fetch contact data logs seamlessly.
*   **Task 4: Session Control & User Authentication** – Restricted administrative dashboards using `Flask-Login` session management, securing specific database visualization interfaces.
*   **Task 5: REST API Endpoint Architecture** – Engineered a scalable public backend API endpoint that dynamically queries underlying tables and serializes data rows into standard JSON arrays.

---

## Technology Stack & Dependencies

*   **Core Backend:** Python 3.x, Flask Web Engine
*   **Security Modules:** Flask-Login
*   **Relational Engine:** SQLite3 (Serverless Relational Database)
*   **Frontend UI:** Jinja2 Template Framework, Bootstrap 5 CSS Ecosystem

---

## Repository Workspaces Directory

```text
barakah_flask_project/
│
├── app.py                  # Primary backend server file & routing configurations
├── messages.db             # Automated transactional SQLite binary datafile
└── templates/              # Jinja2 template workspace views
    ├── layout.html         # Master layout wireframe containing global nav views
    ├── home.html           # Task 1: Welcome portal module view
    ├── contact.html        # Task 2 & 3: Input portal interface for form logging
    ├── login.html          # Task 4: User authentication control screen
    └── messages.html       # Task 3: Protected admin data grid dashboard panel
```

---

##  Installation & Execution Guide

Follow these sequential steps to run this application workspace locally:

1. **Clone or Download the Project Workspace**
2. **Launch Terminal inside the Project Root Workspace and Install Required Packages:**
   ```bash
   pip install flask flask-login
   ```
3. **Execute the Application Server:**
   ```bash
   python app.py
   ```
4. **Access the Portal via Web Browser:**
   Open your browser workspace and navigate to: `http://127.0.0`

---

##  Secure Testing Profile Credentials

To bypass authorization barriers and evaluate the protected Admin Dashboard Panel (Task 3 & 4), apply the following standard system check logs:
*   **Username:** `zoha`
*   **Password:** `scholarship2026`
