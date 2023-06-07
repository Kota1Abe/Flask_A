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
        if not re.match('^[-]{0,1}[0123456789]+$', salaly_str):
            flash("数値を入力してください")
            return redirect(url_for("input"))
        
        salaly = int(salaly_str)
        
        if 10000000000 < salaly:
            flash("給与には最大、9,999,999,999円で入力可能です")
            return redirect(url_for("input"))
        elif salaly < 0 :
            flash("給与にはマイナスの値は入力できません")
            return redirect(url_for("input"))

        if salaly < 1000000:
            text = "給与：{2}円の場合、支給額:{0}円、税額:{1}円です。".format(int(salaly * 0.9), int(salaly * 0.1), salaly)
            print(text, end="")
        else:
            text = "給与：{2}円の場合、支給額:{0}円、税額:{1}円です。".format(int((salaly - 1000000) * 0.8 + 900000), int((salaly - 1000000) * 0.2 + 100000), salaly)
            print(text, end="")
        return render_template("output.html", text=text)
    
    return redirect(url_for("input"))