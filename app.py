import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
# Secret key is required for session management and flash messages
app.config['SECRET_KEY'] = 'barakah_secret_key_123'

# ===== TASK 4: Flask-Login Configuration =====
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Mock Database for Users (Task 4 Demo purposes)
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Dummy user database records
users_db = {
    '1': User('1', 'admin', 'password123'),
    '2': User('2', 'zoha', 'scholarship2026')
}

@login_manager.user_loader
def load_user(user_id):
    return users_db.get(user_id)


# ===== TASK 3: SQLite Database Setup =====
def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    # Creating a table to store contact form submissions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database file when app starts
init_db()


# ===== TASK 1: Routes & Jinja2 Rendering =====
@app.route('/')
def home():
    return render_template('home.html', title="Home - Flask Portfolio App")


# ===== TASK 2 & 3: Form Handling & Database Integration =====
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')
        
        # TASK 3: Saving data into SQLite Database
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)', 
                       (user_name, user_email, user_message))
        conn.commit()
        conn.close()
        
        return render_template('contact.html', title="Contact Us", success=True, name=user_name)
    
    return render_template('contact.html', title="Contact Us", success=False)


# ===== TASK 3: View Database Records Route =====
@app.route('/admin/messages')
@login_required # TASK 4 restriction: Only logged-in users can view messages
def view_messages():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    all_messages = cursor.fetchall()
    conn.close()
    return render_template('messages.html', title="Admin Dashboard", messages=all_messages)


# ===== TASK 4: User Authentication (Login / Logout) =====
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validating user from our mock dictionary database
        for user_id, user_obj in users_db.items():
            if user_obj.username == username and user_obj.password == password:
                login_user(user_obj)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('view_messages'))
        
        flash('Invalid username or password.', 'danger')
    return render_template('login.html', title="User Login")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


# ===== TASK 5: REST API Endpoint =====
@app.route('/api/v1/messages', methods=['GET'])
def get_messages_api():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, message FROM contacts')
    rows = cursor.fetchall()
    conn.close()
    
    # Structuring data into a clean JSON array list
    output = []
    for row in rows:
        output.append({
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'message': row[3]
        })
    
    # Returning clean JSON data object
    return jsonify({'status': 'success', 'data': output, 'count': len(output)})


if __name__ == '__main__':
    app.run(debug=True)
