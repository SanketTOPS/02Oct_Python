from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/tempdb"

db = SQLAlchemy(app)  # DB Init


# DB Model
class studinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    city = db.Column(db.String(20))
    sub = db.Column(db.String(20))


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nm = request.form["name"]
        ct = request.form["city"]
        sub = request.form["sub"]

        stdata = studinfo(name=nm, city=ct, sub=sub)
        db.session.add(stdata)
        db.session.commit()
        print("Record Inserted!")
    else:
        print("Error!")
    return render_template("index.html")


@app.route("/showdata")
def showdata():
    stdata = studinfo.query.all()
    return render_template("showdata.html", stdata=stdata)


@app.route("/deletedata/<int:id>", methods=["GET"])
def deletedata(id):
    stid = studinfo.query.get_or_404(id)
    db.session.delete(stid)
    db.session.commit()
    print("Record Deleted!")
    return redirect("/showdata")


if __name__ == "__main__":
    app.run(debug=True, port=5600)
