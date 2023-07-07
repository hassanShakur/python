from flask import Flask, render_template

app = Flask(__name__)
list = [1, 2, 3]


@app.route("/")
def home():
    return render_template("index.html", text="Hello world", nums=list)


@app.route("/hello/<name>")
def greeter(name):
    return f"Hello {name.title()}"


if __name__ == "__main__":
    app.run(debug=True)

    