from flask import Flask, json, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Load configuration from JSON file
with open('config.json', 'r') as f:
    params = json.load(f)['params']

# Setting configuration for sending mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = params['gmail-user']
app.config['MAIL_PASSWORD'] = params['gmail-password']
app.config['MAIL_USE_TLS'] = True  # Transport Layer Security
app.config['MAIL_USE_SSL'] = False  # Secure Sockets Layer

mail = Mail(app)

@app.route('/')
def mail_function():
    return render_template('mailform.html')

@app.route('/send_email', methods=['POST'])
def send_mail():
    recipient = request.form['recipient']
    subject = request.form['subject']
    body = request.form['body']
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.body = body
    mail.send(msg)
    return 'Message sent Successfully'

app.run(debug=True)