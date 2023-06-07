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
def login_required(view):
    @wraps(view)
    def inner(*args,**kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view(*args,**kwargs)
    return inner
"""

"""
@app.route("/registration",methods=["GET","POST"])
def registration():
    if request.method=="POST":
        if request.form["username"]!=app.config["USERNAME"]:
            flash("ユーザー名が異なります")
        elif request.form["password"]!=app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            session["logged_in"]=True
            flash("ログインしました")
            return redirect(url_for('show_entries'))
    return render_template("input.html")
"""

"""
@app.route("/logout")
def logout():
    session.pop("logged_in",None)
    flash("ログアウトしました")
    return redirect(url_for('show_entries'))
"""
