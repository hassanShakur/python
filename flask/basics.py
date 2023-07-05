from flask import Flask

# __name__ refers to the current file we are working on
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


if __name__ == "__main__":
    app.run()
