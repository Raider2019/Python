from flask import Flask, render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

#Представлення
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
  #
@app.route('/contacts')
def contacts():
    return render_template("contatcts.html")


#Start
