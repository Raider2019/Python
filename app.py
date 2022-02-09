from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, StringField,EmailField, TelField,DateField, TimeField,DecimalField
from wtforms.validators import DataRequired,Email,NumberRange, ValidationError


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b\x1aL\x05}\xe6\xfb\xf2\xd5\x13`S\x89\x8f/\xc5\xfcO\x93fN?\xe1\xa1\xe1\x0b\x01\xf7\x88Y\x12\xbe|' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Perevoski.db'
db = SQLAlchemy(app)
 
#Модель
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255) )
    email = db.Column(db.String(120))
    namber_phone = db.Column(db.String(11))
    type_wantazy = db.Column(db.String(150))
    weight = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    city_start = db.Column(db.String(50))
    city_finish =  db.Column(db.String(50))
    street_start  =  db.Column(db.String(150))
    street_finish  =  db.Column(db.String(150))
    pay_method =  db.Column(db.String(50))

#Форма
class ApplicationForm(FlaskForm):
    name = StringField(label= 'Ваше ім`я', validators = [DataRequired()],render_kw = {"placeholder": "ПІБ"},)
    email = EmailField(label='Ваша електрона адреса',validators = [DataRequired(), Email()])
    namber_phone = TelField(label='Ваш номер телефона' , validators = [DataRequired()] )
    type_wantazy = StringField(label='Вантаж', validators = [DataRequired()],render_kw={"placeholder":"Вкажіть товар якій треба доставити"} )
    weight = IntegerField(label='Вага вантажу',validators = [DataRequired(), NumberRange(min=10,max=10000)],render_kw={"placeholder":"  кг абр тонн"})
    date = DateField(label="Дата відправлення",validators = [DataRequired()],format = '%Y-%m-%d')
    time = TimeField(label="Час відправлення",validators = [DataRequired()],format = '%H:%M')
    city_start = StringField(label= "Місто відправника", validators = [DataRequired()] )
    street_start = StringField(label= "Вулиця відправника", validators = [DataRequired()] )
    city_finish = StringField(label= "Місто отримувача", validators = [DataRequired()])
    street_finish = StringField(label= "Вулиця отримувача", validators = [DataRequired()])
    pay_method = StringField(label= "Спосіб оплати", validators = [DataRequired()])

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = ApplicationForm()
    if form.validate_on_submit():
            user =  User(name = form.name.data, email = form.email.data, namber_phone = form.namber_phone.data, type_wantazy = form.type_wantazy.data, date = form.date.data,
        city_start = form.city_start.data, street_start = form.street_start.data, city_finish = form.city_finish.data, street_finish = form.street_finish.data, 
        pay_method = form.pay_method.data, weight = form.weight.data, time = form.time.data)
            db.session.add(user)
            db.session.commit()
     
            return redirect("/")
    return render_template('index.html',form = form)
@app.route('/contacts')
def contacts():
    return render_template("contatcts.html")

@app.route('/price')
def price():
    return render_template("price.html")

if  __name__ == "__main__":
        app.run(DEBUG = True)