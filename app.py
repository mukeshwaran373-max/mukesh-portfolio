from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
import os  

SENDER_EMAIL = os.environ.get('GMAIL_USER')
SENDER_PASSWORD = os.environ.get('GMAIL_PASS')
RECEIVER_EMAIL = os.environ.get('GMAIL_USER')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Email content
    subject = f"Portfolio Contact from {name}"
    body = f"""
You got a new message from your portfolio website:

Name: {name}
Email: {email}
Message: {message}
"""
    
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print("Email sent successfully!")
        return redirect(url_for('home', success=True))
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return redirect(url_for('home', error=True))

if __name__ == '__main__':
    app.run(debug=True)
