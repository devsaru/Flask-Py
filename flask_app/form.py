from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/',methods=['GET'])
def test_form():
    return render_template('testform.html')

form_data = []

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        form_data.append({'name':name,'age':age,'city':city})
        return redirect(url_for('display_data'))

@app.route('/data')
def display_data():
    return render_template('data.html',test_data=form_data)      


app.run(debug=True)



#iterate a given list and check if a given element exits as a key value in a dictionary.if not, delete it

#roll_dict=[47,64,69,37,78,83,95,97]
#sample_dict={'John':47,'Emma':69,'kelly':76,'Jason:97'}