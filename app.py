from flask import Flask, render_template, request
import smtplib
import os
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    SENDER_EMAIL = os.environ.get('GMAIL_USER')
    SENDER_PASSWORD = os.environ.get('GMAIL_PASS')
    
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        return "ERROR: Env variables set aagala"
    
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    try:
        msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg['Subject'] = f"Portfolio Contact from {name}"
        msg['From'] = SENDER_EMAIL
        msg['To'] = SENDER_EMAIL

        # RENDER KU IDHU DHAN WORK AAGUM - PORT 465 SSL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # <-- CHANGE 1
        server.login(SENDER_EMAIL, SENDER_PASSWORD)        # <-- CHANGE 2: starttls illa
        server.send_message(msg)
        server.quit()
        
        return "Message sent successfully! Thanks da thalaiva."
    except Exception as e:
        return f"ERROR: {str(e)}"
