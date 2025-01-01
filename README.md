# Voice-Based Form Filling 

This is a Flask-based web application that leverages OpenAI's Whisper model for transcribing audio input to text. The app enables users to complete forms using voice input by processing audio files, extracting transcriptions, and mapping the text to form fields.  

The application includes user authentication (signup and login pages), a home page, and a registration form page.

**Deployment Link**: [Voice Form Filling App](https://form-filling-project-gba3.onrender.com)  
**Screen Recording Link**: [Demo Video](https://drive.google.com/file/d/1aibOASPsC-OzpsLcru2JeKZ5nkHZQQN4/view?usp=sharing)

---

### Workflow

1. **Signup**: After the user submits their signup details, the system checks if the provided email is already present in the database.

   - If the email already exists, the user is redirected to the signup page.
   - If it’s a new email, the user can proceed to the login page.

3. **Login**: When the user tries to log in:
   - If the credentials are incorrect, the user is redirected back to the login page to try again.
   - If the credentials are correct, the student registration form opens for the user to fill out.

4. **Student Registration Form**: 
   - After filling out the student registration form, the system checks if all details are valid.
   - If the form is valid, the user is redirected to the home page.
   - If the form is invalid or incomplete, the user is redirected back to the form page to correct the errors.
     
---

## Features

- **Voice-to-Text Transcription**: Uses OpenAI's Whisper model to transcribe audio files into text.
- **Field-Specific Processing**: Automatically adapts transcription for fields like email addresses (e.g., replacing "at the rate" with "@" and "dot" with ".").
- **User Authentication**: Secure signup and login system.
- **User-Friendly Pages**:
   - **Home Page**: Serves as the central hub for navigation.
                 ![image](https://github.com/user-attachments/assets/76e9d298-b912-400a-8f5f-8719359ed331)

  - **Signup Page**: Allows new users to create accounts.
               ![image](https://github.com/user-attachments/assets/ecc45ccf-7ab8-4a73-8e81-dd79cd81a423)

  - **Login Page**: Authenticates returning users.
                ![image](https://github.com/user-attachments/assets/cce0cc51-6eeb-4a7d-b428-31824cbc605e)

  - **Registration Form Page**: Provides the interface for voice-based form filling.
                ![image](https://github.com/user-attachments/assets/967fa02c-21cf-4e7f-b305-40522cebe7cd)
---

## Prerequisites
- Python 3.8 or higher
- MySQL database
- pip (Python package installer)

---

## Installation

### 1. Clone the Repository
```bash
https://github.com/yourusername/voice-form-filling.git
cd voice-form-filling
```

### 2. Install Dependencies
Ensure you have all necessary dependencies installed by using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Download Whisper Model
The application uses the "tiny" version of Whisper. This will be downloaded automatically when you run the app.

---

## Usage

### 1. Run the Application
```bash
python app.py
```

### 2. Access the Application
Open a browser and navigate to:
```
http://127.0.0.1:5000
```
---

## Deployment
The application is deployed on platform[Render](https://render.com). However, due to memory constraints on free-tier deployments, the audio upload feature might not work reliably.

