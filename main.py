from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test01.db'
db = SQLAlchemy(app)
 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/contacts')
def contacts():
    return render_template("contatcts.html")

if  __name__ == "__main__":
        app.run(DEBUG = True)