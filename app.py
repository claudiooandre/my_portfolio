from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for using flash messages

# Email configurations (replace with your details)
EMAIL_ADDRESS = <email>
EMAIL_PASSWORD = <pass>

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            # Configure the email
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = EMAIL_ADDRESS  # Send to your own email
            msg['Subject'] = f"Website contact from {name}"

            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            # Send email using SMTP
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            flash('Message sent successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'An error occurred while sending the message: {e}', 'danger')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
