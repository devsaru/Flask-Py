from flask import Flask,json
from flask_mail import


app = Flask(__name__)
with open('config.json','r') as f:
    params = json.load(f)['params']

#Setting confrigation for sending mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = params['gmail-user']
app.config['MAIL_PASSWORD'] = params['gmail-password']
app.config['MAIL_USE_TLS'] =True #Transport Layer Security
app.config['MAIL_USE_TLS'] =False # Secured Socket Layer

mail = Mail(app)
@app.route('/')
def index():
    msg = Message("Important Mail",
    sender = app.config['MAIL_USERNAME'],
    recipients=['ankitadhakate29@gmail.com'])
    msg.body = "This is to inform you that your fees is pending..!!!"
   # with app.open_resource()
    mail.send(msg)
    return "Message sent successfully"
app.run(debug=True)    


#count all latters.digits and special symbols form a given sysntaxwarning
# i/p: "Prfs$fjg@GF5$#@"
# o/p:

# letters = 
# digits =
# symbols =