from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
from functools import wraps
from holiday.models.mst_holiday import Entry
from holiday import db
#from flask_blog.views.views import login_required

@app.route("/maintenance_date",methods=["GET","POST"])
def maintenance():
    if request.method=="POST":
        if request.form["button"]=="insert_update":

            if request.form["holiday"]=="":
                flash("日付が未入力です。入力してください")
                return redirect("/")
        
            #elif request.form["button"]=="delete":

            else:
                Date=request.form["holiday"]  
                Text=request.form["holiday_text"]

                holiday=Entry(holi_date=Date,holi_text=Text)
                db.session.merge(holiday)
                db.session.commit()

                return render_template("result.html",Date=Date,Text="("+Text+")"+"が登録されました")
        
        elif request.form["button"]=="delete":
            entry=Entry.query.get(request.form["holiday"])
            db.session.delete(entry)
            db.session.commit()
            return redirect(url_for("show_entries"))
        

@app.route("/result",methods=["GET","POST"])
def result():
    return redirect(url_for("show_entries"))