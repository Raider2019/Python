from flask import Flask, render_template

app = Flask(__name__)


#Представлення
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template("contatcts.html")


#Start
    if  __name__ == "__main__":
        app.run(debug=True)