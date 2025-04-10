from flask import Flask, render_template, request
from flask_mysqldb import MySQL

# DB Config.
app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "tempdb"

db = MySQL(app)  # DB Init


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nm = request.form["name"]
        ct = request.form["city"]
        sub = request.form["sub"]

        cr = db.connection.cursor()
        query = f"insert into student(name,city,sub)values('{nm}','{ct}','{sub}')"
        cr.execute(query)
        db.connection.commit()
        print("Record insrted!")
    else:
        print("Error!")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
