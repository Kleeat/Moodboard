from tempfile import mkdtemp

from flask import Flask
import os

from flask_session import Session

from moodborad_app.app.admin import admin
from moodborad_app.app.index import index

app = Flask(__name__)

# App configurations

# Random generated secret key
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = mkdtemp()
app.config['SESSION_FILE_THRESHOLD'] = 500

# Registering route blueprints

app.register_blueprint(index, url_prefix="/")
app.register_blueprint(admin, url_prefix="/")

# Creating a session to be used for authentication

sess = Session(app)

# Lunching the app

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="192.168.1.44")
