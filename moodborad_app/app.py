from flask import Flask
from moodborad_app.app.index import index

app = Flask(__name__)

app.register_blueprint(index, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
