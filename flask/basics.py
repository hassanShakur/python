from flask import Flask

# __name__ refers to the current file we are working on
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world"


# Url parsing and vars
# vars
@app.route("/<string:name>")
def hey_user(name):
    return f"Hello {name}"


@app.route("/<string:name>/<lname>")
def hey_fuser(name, lname):
    return f"Hello {name} {lname}"


# Path
@app.route("/<int:x>/<path:path>")
def print_path(x, path):
    return f"Your path is {x,path}"


if __name__ == "__main__":
    app.run(debug=True)
