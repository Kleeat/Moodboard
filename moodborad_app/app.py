from flask import Flask

from moodborad_app.app.admin import admin
from moodborad_app.app.index import index

app = Flask(__name__)

app.register_blueprint(index, url_prefix="/")
app.register_blueprint(admin, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="192.168.1.44")
