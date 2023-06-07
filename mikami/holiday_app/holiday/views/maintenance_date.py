from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

from holiday import db

from holiday.models.mst_holiday import Holiday

import datetime

import re

@app.route("/maintenance_date/add", methods=["POST"])
def add_date():
    holiday = request.form["holiday"]
    holiday_text = request.form["holiday_text"]

    if holiday_text == "":
        flash("日付テキストの入力は必須です", "danger")
        return redirect(url_for("show_input"))
    elif len(holiday_text) > 20:
        flash("文字列は20文字以内で入力してください", "danger")
        return redirect(url_for("show_input"))

    # 日程の正規化
    # try:
    if not re.match('^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', holiday):
        flash("日付が不正な値です。フォーマット例通りに入力してください(例：2000-01-01)", "danger")
        return redirect(url_for("show_input"))

    holiday_split = holiday.split('-', 3)

    holiday_split[0] = int(holiday_split[0])
    holiday_split[1] = int(holiday_split[1])
    holiday_split[2] = int(holiday_split[2])

    

    tdate = datetime.date(holiday_split[0], holiday_split[1], holiday_split[2])
    
    editHoliday = Holiday.query.get(tdate)

    if not editHoliday == None:
        editHoliday.holi_text = holiday_text
        db.session.merge(editHoliday)
        db.session.commit()
        flash("新しく追加しました", "info")
        return render_template("result.html")
    else: 
        addHoliday = Holiday(
            holi_date = tdate,
            holi_text = holiday_text
        )
        db.session.add(addHoliday)
        db.session.commit()
        flash("新しく追加しました", "info")
        return render_template("result.html")
        
    #finally:
    #    flash("日付が不正な値です。フォーマット例通りに入力してください(例：2000-01-01)", "danger")
    #    return redirect(url_for("show_input"))