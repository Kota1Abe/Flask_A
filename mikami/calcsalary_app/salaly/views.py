from flask import request, redirect, url_for, render_template, flash, session
from salaly import app

# 正規表現用のライブラリ
import re

@app.route("/")
def input():
    return render_template("input.html")

@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == "POST":
        salaly_str = request.form["salaly"]
        if re.match('^[0123456789]+$', salaly_str):
            return "gg"
        return "gg"