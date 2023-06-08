from flask import request, redirect, url_for, render_template, flash, session
from myapp import app, db

from functools import wraps

from myapp.models.user import User
from myapp.models.career import Career
from myapp.models.product import Product

from myapp.views.views import login_required #, user_permission_check

import re

import requests
from bs4 import BeautifulSoup

@app.route("/user/<int:id>/career/add", methods=["GET", "POST"])
@login_required
def add_career(id):
    if not re.match('^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', request.form["s_date"] + "-01"):
        flash("日付が不正な値です。フォーマット例通りに入力してください(例：2000-01)", "danger")
        return redirect(url_for("add_career", id=id))

    if request.method == "POST":
        career = Career(
            user_id = id,
            name = request.form["name"],
            imgsrc = request.form["imgsrc"],
            position = request.form["position"],
            s_date = request.form["s_date"] + "-01"
        )
        db.session.add(career)
        db.session.commit()
        flash("経歴を追加しました")
        return redirect(url_for("show_user", id=id))
    return render_template("career/input.html")

@app.route("/user/<int:userid>/career/update/<int:careerid>", methods=["GET", "POST"])
@login_required
def update_career(userid, careerid):
    if request.method == "POST":
        if not re.match('^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', request.form["s_date"] + "-01"):
            flash("日付が不正な値です。フォーマット例通りに入力してください(例：2000-01)", "danger")
            return redirect(url_for("update_career", userid=userid, careerid=careerid))
        
        career = Career.query.filter(Career.id == careerid).first()

        career.name = request.form["name"]
        career.imgsrc = request.form["imgsrc"]
        career.position = request.form["position"]
        career.s_date = request.form["s_date"] + "-01"

        db.session.merge(career)
        db.session.commit()
        flash("経歴を更新しました")
        #user = User.query.filter(User.id == id).first()
        #return render_template("career/career.html", user=user)
        return redirect(url_for("show_user", id=userid))
    
    career = Career.query.filter(Career.id == careerid).first()
    return render_template("career/update.html", career=career)

@app.route("/user/<int:userid>/career/delete/<int:careerid>", methods=["POST"])
@login_required
def delete_career(userid, careerid):
    career = Career.query.filter(Career.id == careerid).first()
    db.session.delete(career)
    db.session.commit()
    flash("経歴を削除しました")
    return redirect(url_for("show_user", id=userid))


@app.route("/user/<int:id>/career/add_w", methods=["GET", "POST"])
@login_required
def add_w_career(id):
    if request.method == "POST":
        res = requests.get(request.form["url"])
        soup = BeautifulSoup(res.text, "html.parser")

        # 経歴
        careerSelector = {
            "text": ".fuhLwL span",
            "position": ".eMhnQX h3",
            "img": ".btVpRG img",
            "date_s": "div time:nth-child(1)"
        }

        caree = []

        elems =soup.select(".jxAaMM")

        i = 0
        for elem in elems:
            careelist = {}
            for key in careerSelector.keys():
                if key == "img":
                    print(key)
                    if not bool(elem.select(careerSelector[key])):
                        careelist[key] = None
                        continue
                    print(elem.select(careerSelector[key])[0].attrs["src"])
                    careelist[key] = elem.select(careerSelector[key])[0].attrs["src"]
                elif key == "url":
                    print(key)
                    if not bool(elem.select(careerSelector[key])):
                        careelist[key] = None
                        continue
                    print(elem.select(careerSelector[key])[0].attrs["href"])
                    careelist[key] = elem.select(careerSelector[key])[0].attrs["href"]
                else:
                    print(key)
                    if not bool(elem.select(careerSelector[key])):
                        careelist[key] = None
                        continue
                    print(elem.select(careerSelector[key])[0].string)
                    careelist[key] = elem.select(careerSelector[key])[0].string
            caree.append(careelist)
            i += 1
        
        manth = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }

        for value in caree:
            m = value["date_s"][0:3]
            y = value["date_s"][4:8]
            value["date_s"] = y + "-" + manth[m]


        print(caree)
        session["n"] = len(caree)
        return render_template("career/update_w.html", id=id, caree=caree)
        #return redirect(url_for("show_user", id=userid))
    return render_template("career/add_w.html", id=id)

@app.route("/user/<int:id>/career/add_wpost", methods=["POST"])
@login_required
def add_wpost_career(id):
    for key in range(session["n"]):
        key = str(key)
        if not re.match('^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', request.form["s_date["+key+"]"] + "-01"):
            flash("日付が不正な値です。フォーマット例通りに入力してください(例：2000-01)", "danger")
            return render_template("career/add_w.html", id=id)

        if request.method == "POST":
            career = Career(
                user_id = id,
                name = request.form["name["+key+"]"],
                imgsrc = request.form["imgsrc["+key+"]"],
                position = request.form["position["+key+"]"],
                s_date = request.form["s_date["+key+"]"] + "-01"


            )
            db.session.add(career)
            db.session.commit()
    flash("経歴を追加しました")
    return redirect(url_for("show_user", id=id))
    #return render_template("career/input.html")