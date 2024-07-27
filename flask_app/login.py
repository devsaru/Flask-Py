from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/form',methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/login',methods=['POST'])

def login():
    username = request.form['username']
    passwd = request.form['passwd']


    if username == 'Sarita' and passwd == '12345' :
        return f'You have logged in successfully,{username}'
    else:
        return 'Invalid Credentials, please try again'


app.run(debug=True)
