from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/market')
def market():
    return render_template("market.html")


@app.route('/user')
def user():
    return render_template("user.html")

@app.route('/item')
def item():
    return render_template("item.html")

@app.route('/sell')
def sell():
    return render_template("sell.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')