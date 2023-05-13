from flask import Blueprint, render_template, request, redirect, url_for, Response, session

import yaml
from yaml.loader import SafeLoader

from moodborad_app.moods import moods, set_mood

admin = Blueprint("admin", __name__)

# Load admin dict from the admins.yaml file

admins = yaml.load(open("admins.yaml"), Loader=SafeLoader)


# Login route that displays the login screen
@admin.route("/login", methods=['GET'])
def login_view():
    # If user is logged in redirect to select else show login screen
    if session.get("user"):
        return redirect(url_for('admin.select_mood'))
    else:
        return render_template("login.html")


# Login route to log the user in
@admin.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password matches one on the admins.yaml file
    if username in admins.keys() and password == admins.get(username):
        # Save the username to the server-side session
        session['user'] = username
        return redirect(url_for('admin.select_mood'))
    else:
        return render_template("login.html"), 401


# Logout route to log the user out
@admin.route("/logout", methods=['GET', 'POST'])
def logout():
    # Delete the current username form the session
    session['user'] = None
    return redirect(url_for('index.home'))


# Mood route to select the new mood
@admin.route("/mood", methods=['GET'])
def select_mood():
    # If user is logged in show selector else return 401
    if session.get("user"):
        mood_names = moods.keys()
        return render_template("selector.html", moods=mood_names)
    else:
        return Response("Unauthorized", status=401)


# Mood route to update the current mood
@admin.route("/mood", methods=['POST'])
def update_mood():
    mood = request.form.get('mood')

    # Check if user is logged in
    if session.get("user"):
        set_mood(mood)
        return redirect(url_for('index.home'))
    else:
        return Response("Unauthorized", status=401)
