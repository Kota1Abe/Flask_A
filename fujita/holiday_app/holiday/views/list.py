#一覧画面の呼び出し
from flask import request,redirect,url_for,render_template,flash,session
from holiday import holiday_app
from holiday.models.mst_holiday import HolidayMaster

@holiday_app.route('/list.html',methods=['POST'])
def list():
    entries=HolidayMaster.query.order_by(HolidayMaster.holi_date.asc()).all()
    return render_template('list.html',entries=entries)