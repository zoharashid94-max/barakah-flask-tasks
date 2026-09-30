from flask import Flask, render_template, request

app = Flask(__name__)

# ===== TASK 1: Routes & Jinja2 Rendering =====
@app.route('/')
def home():
    # Jinja2 template ko title variable bhej rahe hain
    return render_template('home.html', title="Home - Barakah TechLabs Task 1")

# ===== TASK 2: Form Handling & POST Request =====
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Form se user ka data nikalna
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')
        
        # Success message ke sath page dikhana
        return render_template('contact.html', title="Contact Us", success=True, name=user_name)
    
    # Agar simple page khola hai to khali form dikhana
    return render_template('contact.html', title="Contact Us", success=False)

if __name__ == '__main__':
    app.run(debug=True)
