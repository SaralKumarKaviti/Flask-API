from flask import Flask,request
from project_data import Register, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json


engine=create_engine('sqlite:///student.db',connect_args={'check_same_thread': False},echo=True)
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

app=Flask(__name__)

app.secret_key='super_secret_key'

@app.route("/newStudent", methods=['POST','GET'])
def addData():
	data_status ={"responseStatus":0,"result":""}
	name = request.json['name']
	surname = request.json['surname']
	email = request.json['email']
	className = request.json['className']
	mobile = request.json['mobile']
	fatherName = request.json['fatherName']
	motherName = request.json['motherName']
	gender = request.json['gender']

	if name and surname and email and className and mobile and fatherName and motherName and gender and request.method=='POST':
		newData=Register(name=name,
			surname=surname,
			email=email,
			className=className,
			mobile=mobile,
			fatherName=fatherName,
			motherName=motherName,
			gender=gender
			)
		session.add(newData)
		session.commit()
		data_status["responseStatus"]=1
		data_status["result"]="Successfully added new student"
		return data_status
	else:

		data_status["responseStatus"]=0
		data_status["result"]="Required fields are missing"
		return data_status

@app.route('/showStudents', methods=['POST','GET'])
def showData():
	data_status ={"responseStatus":0,"result":""}
	student_list=[]
	student_dict={}
	if request.method=="GET":
		register=session.query(Register).all()
		for rg in register:
			student_dict={
				"name":rg.name,
				"surName":rg.surname,
				"gender":rg.gender,
				"email":rg.email,
				"className":rg.className,
				"mobileNumber":rg.mobile,
				"fatherName":rg.fatherName,
				"mobileNumber":rg.motherName
			}
			student_list.append(student_dict)
			
			data_status["responseStatus"]=1
			data_status["result"]=student_list
			
	else:
		data_status["responseStatus"]=0
		data_status["result"]="Data not available"
	return data_status

@app.route("/deleteStudent" ,methods=['DELETE'])
def deleteData():
	data_status ={"responseStatus":0,"result":""}
	register_id = request.json['register_id']
	delData=session.query(Register).filter_by(id=register_id).one()

	if request.method=='DELETE':
		session.delete(delData)
		session.commit()
		data_status["responseStatus"]=1
		data_status["result"]="Successfully Deleted %s" %(delData.name)
		return data_status
	else:
		data_status["responseStatus"]=0
		data_status["result"]="Required fields are missing"
		return data_status

@app.route("/editStudent",methods=['POST'])
def editData():
	data_status ={"responseStatus":0,"result":""}
	register_id = request.json['register_id']
	editedData=session.query(Register).filter_by(id=register_id).one()
	
	if request.method=='POST':
		editedData.name=request.json['name']
		editedData.surname=request.json['surname']
		editedData.email=request.json['email']
		editedData.className=request.json['className']
		editedData.mobile=request.json['mobile']
		editedData.fatherName=request.json['fatherName']
		editedData.motherName=request.json['motherName']
		editedData.gender=request.json['gender']

		session.add(editedData)
		session.commit()
		data_status["responseStatus"]=1
		data_status["result"]="Successfully Edited %s" %(editedData.name)
		# return data_status

	else:
		data_status["responseStatus"]=0
		data_status["result"]="Data not available"
	return data_status
	



if __name__=='__main__':
	app.run(debug=True)




