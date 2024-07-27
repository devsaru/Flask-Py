# from flask import Flask,request,render_template
# from pymongo import MongoClient


# app = Flask(__name__)
# #client = MongoClient('')

# #using MongoAtlas Confriguration
# mongo_url = "mongodb+srv://saru2421:<password>@itsdatabase.rpqtb05.mongodb.net/?retryWrites=true&w=majority&appName=itsdatabase"
# client = MongoClient(mongo_uri)

# db = client['flask-db']
# collection = db ['Users']
# collection1 = db['Index']


# @app.route('/app_data',methods=['POST'])
# def add_data():
#     data = request.json
#     collection.insert_one(data)
#     return 'Data Added to MongoDB'

# @app.route('/')
# def index():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         form_data = {
#             'name':name,
#             'email':email,
#             'password':password
#         }
#         if 'password' in form_data
#         from_data['password']=hashpw(form_data['password'].encode('utf-8'),gensalt())
#         collection.insert_one(form_data)
#         return redirect(url_for('index'))

# app.run(debug=True)        


    