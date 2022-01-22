from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Perevoski.db'
db = SQLAlchemy(app)
 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80) )
    email = db.Column(db.String(120))
    namber_phone = db.Column(db.String(11))
    type_wantazy = db.Column(db.String(150))
    weight = db.Column(db.Integer)
    datatime = db.Column(db.DateTime, default = datetime.now())
    city_start = db.Column(db.String(50))
    city_finish =  db.Column(db.String(50))
    street_start  =  db.Column(db.String(150))
    street_finish  =  db.Column(db.String(150))
    pay_method =  db.Column(db.String(50))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/contacts')
def contacts():
    return render_template("contatcts.html")

if  __name__ == "__main__":
        app.run(DEBUG = True)