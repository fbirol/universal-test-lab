import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
instance_dir = os.path.join(basedir, "instance")
if not os.path.exists(instance_dir):
    os.makedirs(instance_dir)
db_path = os.path.join(instance_dir, "universal_test_lab.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)


VALID_USERNAME = "furkan"
VALID_PASSWORD = "1234"


@app.route("/")
def home():
    return redirect(url_for("list_records"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return redirect(url_for("list_records"))
        else:
            error = "Kullanıcı adı veya şifre yanlış!"
    return render_template("login.html", error=error)


@app.route("/list", methods=["GET"])
def list_records():
    records = Record.query.all()
    return render_template("list.html", records=records)


@app.route("/add", methods=["GET", "POST"])
def add_record():
    error = None
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if not name or not email:
            error = "İsim ve e-posta zorunlu!"
        else:
            new_record = Record(name=name, email=email)
            db.session.add(new_record)
            db.session.commit()
            return redirect(url_for("list_records"))
    return render_template("add.html", error=error)


@app.route("/delete/<int:record_id>", methods=["POST"])
def delete_record(record_id):
    record = db.session.get(Record, record_id)
    if record:
        db.session.delete(record)
        db.session.commit()
        print("Kalan kayitlar:", Record.query.all())
    return redirect(url_for("list_records"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
