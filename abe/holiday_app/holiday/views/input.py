from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
from functools import wraps
from holiday.models.mst_holiday import Entry
from holiday import db
#from flask_blog.views.views import login_required

@app.route('/')
def show_entries():
    #entries=Entry.query.order_by(Entry.id.desc()).all()
    return render_template("input.html") #,entries=entries

"""
@app.route("/maintenance_date",methods=["GET","POST"])
def maintenance():
    if request.method=="POST":
        if request.form["button"]=="insert_update":

            if request.form["holiday"]=="":
                flash("日付が未入力です。入力してください")
                return redirect("/")
        
            else:
                Date=request.form["holiday"]  
                Text=request.form["holiday_text"]
                return render_template("result.html",Date=Date,Text=Text)
            
        #elif request.form["button"]=="delete":
"""

"""
@app.route("/list",methods=["GET","POST"])
def list():
    if request.method=="POST":
        entries=Entry.query.order_by(Entry.holi_date.desc().all())
        return render_template("list.html",entries=entries)
"""


"""
@app.route("/result",methods=["GET","POST"])
def result():
"""
