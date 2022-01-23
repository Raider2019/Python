from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms  import IntegerField, StringField, DateTimeField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b\x1aL\x05}\xe6\xfb\xf2\xd5\x13`S\x89\x8f/\xc5\xfcO\x93fN?\xe1\xa1\xe1\x0b\x01\xf7\x88Y\x12\xbe|' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Perevoski.db'
db = SQLAlchemy(app)
 
#Модель
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

#Форма
class ApplicationForm(FlaskForm):
    name = StringField(label= 'Ваше ім`я', validators = [DataRequired()],render_kw = {"placeholder": "ФІО"},)
    email = StringField(label='Ваша електрона адреса',validators = [DataRequired()])
    namber_phone = StringField(label='Ваш номер телефона', validators = [DataRequired()],render_kw={"placeholder":"+380XXXXXXX"} )
    type_wantazy = StringField(label='Вантаж', validators = [DataRequired()],render_kw={"placeholder":"Вкажіть товар якій треба доставити"} )
    weight = IntegerField(label='Вага вантажу',validators = [DataRequired()],render_kw={"placeholder":"Вкажіть вагу вантажу  кг, тонн"})
    datatime = DateTimeField(label="Дата і час доставкі",format= '%d/%m/%Y %H:%M',validators = [DataRequired()],render_kw={"placeholder":"Вкажіть зручний час і дату відправкі вантажу"} )

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/contacts')
def contacts():
    return render_template("contatcts.html")

if  __name__ == "__main__":
        app.run(DEBUG = True)