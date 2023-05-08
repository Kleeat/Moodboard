from flask import Blueprint, render_template

index = Blueprint("index", __name__)


@index.route("/")
def home():
    return "Hello World!"


@index.route("/test/")
def test():
    return render_template("index.html")
