from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/', methods=['GET','POST'])
def home():
    #return 'Hello, World!'
    #return "<h1>Test view</h1>"
    return render_template("home.html")