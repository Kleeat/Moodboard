from flask import Blueprint, render_template

import moodborad_app.app.moods
from moodborad_app.app.moods import moods

index = Blueprint("index", __name__)


@index.route("/")
def home():
    mood_img = moods.get(moodborad_app.app.moods.current_mood)
    return render_template("index.html", mood_img=mood_img, mood=moodborad_app.app.moods.current_mood)

