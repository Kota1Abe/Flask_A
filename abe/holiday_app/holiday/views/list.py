from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
from functools import wraps
from holiday.models.mst_holiday import Entry
from holiday import db


@app.route("/list",methods=["GET","POST"])
def list():
    entries=Entry.query.order_by(Entry.holi_date.asc()).all()
    return render_template("list.html",entries=entries)

