from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

from holiday import db

@app.route("/maintenance_date")
def maintenance_date():
    return render_template("result.html")