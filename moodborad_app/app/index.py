from flask import Blueprint, render_template

from moodborad_app.moods import moods, get_mood

index = Blueprint("index", __name__)


# Home route where the current mood is displayed
@index.route("/")
def home():
    mood_img = moods.get(get_mood())
    return render_template("index.html", mood_img=mood_img)

