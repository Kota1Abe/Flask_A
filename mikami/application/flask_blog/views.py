from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route("/")
def show_entries():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("ユーザー名が異なります", "danger")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります", "danger")
        else:
            flash("ログインしました", "info")
            session["logged_in"] = True
            return redirect(url_for("show_entries"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("ログアウトしました", "info")
    return redirect(url_for("show_entries"))