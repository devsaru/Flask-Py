from flask import Flask,jsonify,request,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Test User"
    return render_template('index.html',test_name=name)

@app.route('/list')
def list_data():
    list_elements = ['AAAP','TESL','MSE','MICRO','TCS']
    return render_template('list.html',ticker=list_elements)

@app.route('/users')
def user_list():
    user = [
        {'name':'Pratik Sir','age':24,'Trainer':'DSA'},
        {'name':'Nikhil Sir','age':28,'Trainer':'React'},
        {'name':'Sudhir Sir','age':32,'Trainer':'Java/python'},
        {'name':'Saurbh Sir','age':34,'Trainer':'Full Stack'}
    ]


    return render_template('users.html',test_user=user)
@app.route('/dict')
def user_dict():
    user = {
      1:  {'name':'Pratik Sir','age':24,'Trainer':'DSA'},
      2:  {'name':'Nikhil Sir','age':28,'Trainer':'React'},
      3:  {'name':'Sudhir Sir','age':32,'Trainer':'Java/python'},
      4:  {'name':'Saurbh Sir','age':34,'Trainer':'Full Stack'}
    
        
    }
    return render_template('dict.html',dict_user=user)



app.run(debug=True)
        


