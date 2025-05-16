from flask import Blueprint, render_template, request


login_bp = Blueprint('login_page', __name__)

@login_bp.route('/login')
def login_page():
    return render_template('login.html')


@login_bp.route('/login', methods=["POST"])
def login_page_submit():
    print(request.form["username"])
    return 
