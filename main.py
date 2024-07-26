from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


with open('config.json','r')as c:
     Billo=json.load(c)["Billo"]


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:@localhost/portfolio"

db = SQLAlchemy(app) 

class Contact(db.Model):
    table_name='contact'
    Sno=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(80),nullable=False)
    Email=db.Column(db.String(80),nullable=False)
    Subject=db.Column(db.String(80),nullable=False)
    Message=db.Column(db.String(80),nullable=False)



@app.route("/",methods=['GET','POST']) 
def main():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        subj=request.form.get("subject")
        msg=request.form.get("message")
        entry=Contact(Name=name,Email=email,Subject=subj,Message=msg)
        db.session.add(entry)
        db.session.commit()                           
    return render_template('index.html',Billo=Billo)

@app.route("/portfolio") 
def port():                                 
    return render_template('portfolio-details.html',Billo=Billo)

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        subj=request.form.get("subject")
        msg=request.form.get("message")
        entry=Contact(Name=name,Email=email,Subject=subj,Message=msg)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html',Billo=Billo)
if __name__=="__main__":
     app.run(debug=True )
