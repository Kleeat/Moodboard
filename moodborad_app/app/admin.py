from flask import Blueprint, render_template, request, redirect, url_for, Response

import moodborad_app
from moodborad_app.app.moods import moods

admin = Blueprint("admin", __name__)


@admin.route("/login", methods=['GET'])
def login_view():
    return render_template("login.html")


@admin.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == "admin" and password == "password123":
        mood_names = moods.keys()
        return render_template("selector.html", moods=mood_names, username=username, password=password)
    else:
        return Response("Unauthorized", status=401)


@admin.route("/mood", methods=['POST'])
def set_mood():
    mood = request.form.get('mood')
    username = request.form.get('username')
    password = request.form.get('password')

    if username == "admin" and password == "password123":
        moodborad_app.app.moods.current_mood = mood
        return redirect(url_for('index.home'))
    else:
        return Response("Unauthorized", status=401)
