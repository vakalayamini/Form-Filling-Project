from flask import Flask, render_template, request, redirect, flash,session
import os
import whisper
from googletrans import Translator
import mysql.connector
from flask_bcrypt import Bcrypt

# Render port binding
PORT = int(os.getenv("PORT", 5000))
# Flask app setup
app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt(app)  # Initialize Bcrypt for password hashing

# Load the Whisper model
model = whisper.load_model("tiny")

# Translator for multilingual support
translator = Translator()

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mouly@18",  # Replace with your MySQL root password
    database="student_registration_db"
)
cursor = db.cursor()

# Function to transcribe speech and translate it
def transcribe_speech(audio_path, target_language='en'):
    result = model.transcribe(audio_path)
    original_text = result['text']
    if target_language != 'en':
        translated_text = translator.translate(original_text, dest=target_language).text
        return translated_text
    return original_text

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

       # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            flash("Account with this email already exists. Please log in.", "warning")
            return redirect('/login')

        # Hash the password and insert user details
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        cursor.execute(
            "INSERT INTO users (firstname, lastname, email, password, password_hash) VALUES (%s, %s, %s, %s, %s)",
            (firstname, lastname, email, password, password_hash)
        )
        db.commit()
        flash("Signup successful! Please log in.", "success")
        return redirect('/login')
    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the email exists
        cursor.execute("SELECT id, password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and user[1] == password:  # Check if password matches
            session['user_id'] = user[0]  # Store user ID in session
            flash("Login successful!", "success")
            return redirect('/form')
        else:
            flash("Invalid username or password.", "danger")
            return redirect('/login')
    return render_template('login.html')

# Form filling route
@app.route('/form', methods=['GET', 'POST'])
def form_filling():
    if 'user_id' not in session:  # Check if user is logged in
        flash("Please log in to access the form.", "warning")
        return redirect('/login')

    if request.method == 'POST':
        # Collect form data
        student_data = (
            request.form['firstName'], request.form['lastName'],
            request.form['fatherName'], request.form['motherName'],
            request.form['dob'], request.form['gender'],
            request.form['phone'], request.form['email'],
            request.form['bloodGroup'], request.form['address'],
            request.form['branch'], request.form['section'],
            request.form['rollNumber'], request.form['yearOfStudy'],
            request.form['percentage']
        )

        # Insert data into the students table
        cursor.execute("""
            INSERT INTO students (firstname, lastname, father_name, mothername, dob, gender, phone, email,
                                  bloodgroup, address, branch, section, rollno, yearofstudy, percentage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, student_data)
        db.commit()

        flash("Student registered successfully!", "success")
        return redirect('/')
    return render_template('form.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user session
    flash("Logged out successfully.", "info")
    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT,debug=True)