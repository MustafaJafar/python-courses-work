from flask import Flask , render_template as rt , request as req
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email 
from sqlalchemy.sql import func

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/height_collector'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model) :
    __tablename__ = "data"
    id = db.Column(db.Integer , primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__ (self , email_ , height_):
        self.email_ = email_
        self.height_ = height_

@app.route('/') #/ == home page
def home ():
    return rt("index.html")

@app.route('/success' , methods = ['POST']) 
def success ():
    if req.method == 'POST' : 
        email = req.form["email_name"]
        height = req.form["height"]
        
        if db.session.query(Data).filter(Data.email_ == email).count() == 0 :

            data  = Data(email , height)
            db.session.add(data)
            db.session.commit()
            
            avg_height = db.session.query(func.avg(Data.height_)).scalar()
            avg_height = round(avg_height , 2)
            
            count =db.session.query(Data.height_).count() 
            send_email(email , height , avg_height , count )
            
            return rt("success.html")
        else : 
            return rt("index.html" , text = "Seems like we've got something from that email address already!")


if __name__ == "__main__" :
    app.run(debug = True)  #runs on local host
    #app.run(host='0.0.0.0') #runs on local network
    