from distutils.log import debug
from flask import Flask


app = Flask(__name__)


@app.route("/")
def info():
    return "Hi ! It's is Biswajit Mishra"


if __name__ == "__main__":
    app.run(debug=True)
