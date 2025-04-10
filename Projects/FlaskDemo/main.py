from flask import Flask


app = Flask(__name__)  # app initlization


@app.route("/")
def index():
    return "Hello Flask!"


@app.route("/about")
def about():
    return "This is About!"


@app.route("/contact")
def contact():
    return "This is Contact"


if __name__ == "__main__":
    app.run(debug=True)
