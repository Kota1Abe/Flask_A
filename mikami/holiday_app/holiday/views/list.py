from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

from holiday import db

@app.route("/list")
def show_list():
    return render_template("list.html")