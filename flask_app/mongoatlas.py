from flask import Flask,render_template,request
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri ='mongodb+srv://saru2421:Saru@itsdatabase.rpqtb05.mongodb.net/?retryWrites=true&w=majority&appName=itsdatabase'
client = MongoClient(mongo_uri)

db = client['flask-db']
collection = client['Users']

@app.route('/add',methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)
    return 'Data has been added successfully'

app.run(debug=True)    
