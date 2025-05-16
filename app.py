from flask import Flask
from flask import render_template, request, session
from routes.login import login_bp
from flask_login import LoginManager
from database.db import db_work
from flask_restful import Resource, Api


app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)
dbb = db_work("users.db")
api = Api(app)



@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/market')
def market():
    all_items = dbb.get_all_items()
    return render_template("market.html", items=all_items)


@app.route('/user/<login>')
def user(login):
    if dbb.get_password(login) != None:
        return render_template("user.html", login=login)
    else:
        return "No such user"

# @app.route('/item')
# def item():
#     return render_template("item.html")

@app.route('/item/<int:id>')
def item(id):
    item_info = dbb.get_item(id)
    return render_template("item.html", item=item_info)



@app.route('/profile')
def profile_red():
    return render_template("login.html")
# @app.route('/sell')
# def sell():
#     return render_template("sell.html")


@app.route('/sell', methods=["POST"])
def sell_submit():
    item_name = request.form["item_name"]
    item_model = request.form["item_model"]
    item_background = request.form["item_background"]
    item_symbol = request.form["item_symbol"]
    item_price = request.form["item_price"]
    item_contact_info = request.form["item_contact_info"]    
    item_description = request.form["item_description"]
    dbb.add_item(item_name, item_model, item_background, item_symbol, item_price, item_contact_info, item_description)
    print(item_name, item_model, item_background, item_symbol, item_price, item_contact_info, item_description)
    return render_template("sell.html")

@app.route('/sell')
def sell():
    return render_template("sell.html")


@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/reg', methods=["POST"])
def reg_submit():
    # email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    c_password = request.form["confirm_password"]
    if dbb.get_password(username) == None:
        if password == c_password:
            dbb.registrate_user(username, password)
    # print(dbb.get_password(username))
    # print(username, password, c_password)

    else:
        print("ts mf exists already")
    
    print(dbb.get_password(username))
    print(username, password, c_password)
    return render_template("reg.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login', methods=["POST"])
def login_submit():
    # email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    print(username, password, dbb.get_password(username))
    print(password == dbb.get_password(username))
    if dbb.get_password(username) == password:
        return render_template("profile.html")
    else:
        return render_template("login.html")

# @app.route('/debug', methods=["POST"])
# def deb():
#     print(request.form["username"])
#     print(1)
#     return "debbuging"

# @login_manager.user_loader
# @app.route("/login", methods=["POST"])
# def load_user():



# app.register_blueprint(login_bp)


class HelloWorld(Resource):
    def get(self):
        print(1)
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api/test')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')