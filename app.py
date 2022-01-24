from flask import Flask, render_template,redirect,url_for
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
    datatime = db.Column(db.String(20))
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
    weight = IntegerField(label='Вага вантажу',validators = [DataRequired()],render_kw={"placeholder":"  кг, тонн"})
    datatime = StringField(label="Дата і час доставкі",validators = [DataRequired()],render_kw={"placeholder":"ДД/ММ/РР ГГ:ММ"} )
    city_start = StringField(label= "Місто відправника", validators = [DataRequired()] )
    street_start = StringField(label= "Вулиця відправника", validators = [DataRequired()] )
    city_finish = StringField(label= "Місто отримувача", validators = [DataRequired()])
    street_finish = StringField(label= "Вулиця отримувача", validators = [DataRequired()])
    pay_method = StringField(label= "Спосіб оплати", validators = [DataRequired()])



@app.route('/', methods = ['GET', 'POST'])
def index():
    form = ApplicationForm()
    if form.validate_on_submit():
            user =  User(name = form.name.data, email = form.email.data, namber_phone = form.namber_phone.data, type_wantazy = form.type_wantazy.data, datatime = form.datatime.data,
        city_start = form.city_start.data, street_start = form.street_start.data, city_finish = form.city_finish.data, street_finish = form.street_finish.data, 
        pay_method = form.pay_method.data, weight = form.weight.data)
            db.session.add(user)
            db.session.commit()
     
            return redirect("/")
    return render_template('index.html',form = form)
@app.route('/contacts')
def contacts():
    return render_template("contatcts.html")

if  __name__ == "__main__":
        app.run(DEBUG = True)