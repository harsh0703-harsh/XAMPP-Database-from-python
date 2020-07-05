from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/dumped'
db=SQLAlchemy(app)
# S. no Name	Branch	Message	Date	Email
class Harsh(db.Model):
	Serial_no=db.Column(db.Integer,primary_key=True)
	Name=db.Column(db.String(30),nullable=False)
	Phone_number=db.Column(db.Integer,nullable=False)
	Branch=db.Column(db.String(20),nullable=False)
	Message=db.Column(db.String(200),nullable=False)
	Date=db.Column(db.String(100))
	Email=db.Column(db.String(200),nullable=False)
	
@app.route("/",methods=['GET','POST'])
def home():
	if request.method=='POST':
		NAME=request.form.get("NAME")
		Phone_Number=request.form.get("Phone_Number")
		Email=request.form.get("Email")
		branch=request.form.get("branch")
		message=request.form.get("message")
		entry=Harsh(Name=NAME,Phone_number=Phone_Number,Email=Email,Branch=branch,Message=message,Date=datetime.now())
		db.session.add(entry)
		db.session.commit()
		if db.session.commit()==True:
			print("Added succesfully")
	return render_template("index.html")

app.run(debug=True)
