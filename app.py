from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# UN GMAIL DETAILS INGE PODU
SENDER_EMAIL = "mukeshwaran373@gmail.com"        # ← Your Gmail address (must be the same as the one used to generate the app password)
SENDER_PASSWORD = "fmwo ivrh zayh latf"       # ←  App password generated from Gmail (not your regular password) - see instructions below
RECEIVER_EMAIL = "mukeshwaran373@gmail.com"      # ← Receiver's email (can be the same as sender for testing)

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