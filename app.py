from flask import Flask
from flask import render_template, request, session
from routes.login import login_bp
from flask_login import LoginManager


app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)

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

@app.route('/reg', methods=["POST"])
def reg_submit():
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["email"]
    
    print(email, username, password)
    return render_template("reg.html")

# @app.route('/login')
# def login():
#     return render_template("login.html")

# @app.route('/debug', methods=["POST"])
# def deb():
#     print(request.form["username"])
#     print(1)
#     return "debbuging"

# @login_manager.user_loader
# @app.route("/login", methods=["POST"])
# def load_user():



app.register_blueprint(login_bp)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')