from flask import request, redirect, url_for, render_template, flash, session
from myapp import app, db

from functools import wraps

from myapp.models.user import User
from myapp.models.career import Career
from myapp.models.product import Product

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter(User.name == request.form["username"], User.password == request.form["password"]).first()

        if user == None:
            flash("ユーザー名かパスワードが異なります", "danger")
            return redirect(url_for("login"))
        else:
            flash("ログインしました", "info")
            session["logged_in"] = True
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/signin", methods=["POST"])
def signin():
    user = User.query.filter(User.name == request.form["username"]).first()
    if not user == None:
        flash("既に同名のユーザーが存在します", "danger")
        return redirect(url_for("login"))

    user = User(
        name = request.form["username"],
        password = request.form["password"]
    )
    db.session.add(user)
    db.session.commit()
    session["logged_in"] = True
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("ログアウトしました", "info")
    return redirect(url_for("show_entries"))

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return inner

@app.route("/")
@login_required
def index():
    user_list = User.query.order_by(User.id.desc()).all()
    return render_template("index.html", user_list = user_list)

@app.route("/user/<int:id>")
@login_required
def show_user(id):
    user = User.query.filter(User.id == id).first()
    return render_template("career/career.html", user=user)

@app.route("/user/<int:id>/update", methods=["GET", "POST"])
@login_required
def update_user(id):
    user = User.query.filter(User.id == id).first()
    if request.method == "POST":
        user.text = request.form["text"]
        user.url = request.form["url"]
        user.imgsrc = request.form["imgsrc"]
        db.session.merge(user)
        db.session.commit()
        return redirect(url_for("show_user", id=id))
    return render_template("update.html", user=user)
    