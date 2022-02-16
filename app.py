from flask import Flask, render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField,EmailField, TelField,DateField,DecimalField, SelectField, SearchField,RadioField,SubmitField
from wtforms.validators import DataRequired,Email,NumberRange, length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b\x1aL\x05}\xe6\xfb\xf2\xd5\x13`S\x89\x8f/\xc5\xfcO\x93fN?\xe1\xa1\xe1\x0b\x01\xf7\x88Y\x12\xbe|' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Perevoski.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
#Модель

class Citys(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     region = db.Column(db.String(255))

     def __repr__(self):
        return '<Region %r>' % self.region



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255) )
    email = db.Column(db.String(120))
    namber_phone = db.Column(db.String(13))
    type_wantazy = db.Column(db.String(150))
    weight = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.String(6))
    date_dostavki = db.Column(db.String(20), default = "-")
    city_start = db.Column(db.String(150),db.ForeignKey('citys.id'))
    city_finish =  db.Column(db.String(150),db.ForeignKey('citys.id'))
    street_start  =  db.Column(db.String(150) )
    number_home_start = db.Column(db.Integer)
    street_finish  =  db.Column(db.String(150))
    number_home_finish = db.Column(db.Integer)
    pay_method =  db.Column(db.String(50))
    isActive = db.Column(db.String(60), default = "В обробці" )

    def __repr__(self):
        return '<Name %r>' % self.name, '<City %r>' %  self.city_finish


#Форма
class ApplicationForm(FlaskForm):
    name = StringField(label= 'Ваше ім`я', validators = [DataRequired()],render_kw = {"placeholder": "ПІБ"},)
    email = EmailField(label='Ваша електрона адреса',validators = [DataRequired(), Email()])
    namber_phone = TelField(label='Ваш номер телефона' , validators = [DataRequired()],render_kw={"placeholder":"+380XXXXXXXXX"} ,)
    type_wantazy = StringField(label='Вантаж', validators = [DataRequired()],render_kw={"placeholder":"Вкажіть товар якій треба доставити"} )
    weight = IntegerField(label='Вага вантажу',validators = [DataRequired(), NumberRange(min=10,max=10000)],render_kw={"placeholder":"  кг абр тонн"})
    date = DateField(label="Дата відправлення",validators = [DataRequired()],format = '%Y-%m-%d')
    time = StringField(label="Час відправлення",validators = [DataRequired(), length(max=5)],render_kw={"placeholder":" гг:мм"})
    city_start = SelectField(label= "Місто відправника(селище)",choices=[],validators = [DataRequired()])
    street_start = StringField(label= "Вулиця відправника", validators = [DataRequired()],render_kw={"placeholder":"Вкажіть вулицю"}  )
    number_home_start = StringField(label= "Номер будинку відправника")
    city_finish = SelectField(label= "Місто отримувача(селище)",choices=[],validators = [DataRequired()])
    street_finish = StringField(label= "Вулиця отримувача", validators = [DataRequired()])
    number_home_finish = StringField(label= "Номер будинку отримувача")
    pay_method = RadioField(label= "Спосіб оплати", validators = [DataRequired()],choices=[('description'),('whatever')]) 
    submit = SubmitField('Sign In')

class AppCheck(FlaskForm):
      email = SearchField(label='Ваша електрона адреса',validators = [DataRequired(), Email()])
      submit = SubmitField('Sign In')

"""
def get_street():
    street_list = []

    street = Addres.query.all()
    for s in street:
        street_list.append((s.id, s.region))
        return street_list

"""

@app.route('/', methods = ['GET', 'POST'])
def index():

    form = ApplicationForm()
    form.city_start.choices =  [(s.region) for s in Citys.query]
    form.city_finish.choices =  [(s.region) for s in Citys.query]
    if form.validate_on_submit():
            user =  User(name = form.name.data, email = form.email.data, namber_phone = form.namber_phone.data, type_wantazy = form.type_wantazy.data, date = form.date.data,
        city_start = form.city_start.data, street_start = form.street_start.data, city_finish = form.city_finish.data, street_finish = form.street_finish.data, 
        pay_method = form.pay_method.data, weight = form.weight.data, time = form.time.data, number_home_start = form.number_home_start.data, number_home_finish = form.number_home_finish.data)
            db.session.add(user)
            db.session.commit()
     
            return redirect("/")
    return render_template('index.html',form = form)
@app.route('/contacts')
def contacts():
    return render_template ("contatcts.html")

@app.route('/price')
def price():
    return render_template("price.html")
    
@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = AppCheck(request.form)

    if form.validate_on_submit():
        result = User.query.filter_by(email = form.email.data).order_by(User.id.desc()).limit(10)
        return render_template('result.html', app  = result)


    return render_template("search.html", form = form)





if  __name__ == "__main__":
        app.run(DEBUG = True)