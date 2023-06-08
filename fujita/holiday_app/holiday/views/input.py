#入力画面の呼び出し
from flask import request,redirect,url_for,render_template,flash,session
from holiday import holiday_app
@holiday_app.route('/')
def show_entries():
    return render_template('input.html')

@holiday_app.route('/input.html',methods=['POST'])
def input():
    return render_template('input.html')
