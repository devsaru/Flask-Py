from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from pymongo import MongoClient
import json
from bson.objectid import ObjectId
from bson.json_util import dumps


app = Flask(__name__)
api = Api(app)

mongo_uri ='mongodb+srv://saru2421:Saru@itsdatabase.rpqtb05.mongodb.net/?retryWrites=true&w=majority&appName=itsdatabase'
client = MongoClient(mongo_uri)

db = client['flask-db']
collection = db['Employees']


# employees = []

class EmployeeAPI(Resource):
    def get(self):
        employees = json.loads(dumps(collection.find({},{'_id':0})))
        return employees,200
  

    # def get(self):
    #     #return{'Hello':'World'}
    #     return employees
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("ID",type=int,required=True,help='Name cannot be blank')
        parser.add_argument("Name",type=str,required=True,help='Name cannot be blank')
        parser.add_argument("Age",type=int,required=True,help="Age cannot be blank")
        parser.add_argument("Department",type=str,required=True,help="Department cannotbe blank")

        data = parser.parse_args()

        if collection.find_one({'ID':data['ID']}):
                return{'message':f"Employee with the name {data['Name']} already exists.!!!"},400

        new_employee = {
            'ID':data['ID'],
            'Name':data['Name'],
            'Age':data['Age'],
            'Department':data['Department']
        } 
        result = collection.insert_one(new_employee)
        new_employee['_id'] = str(result.inserted_id)
        return new_employee,201


class SingleEmployeeAPI(Resource):
    def get(self,ID):
        for employee in employees:
            if employee['ID'] == ID:
                return employee,200
        return {'message':'Employee not found'},404


api.add_resource(EmployeeAPI,'/')
api.add_resource(SingleEmployeeAPI,'/employees/<int:ID>')

if __name__ == '__main__':
    app.run(debug=True)
    
