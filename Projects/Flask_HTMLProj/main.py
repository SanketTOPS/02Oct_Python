from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    name = "Ashok"
    num = random.randint(1111, 9999)
    return render_template("index.html", nm=name, num=num)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
