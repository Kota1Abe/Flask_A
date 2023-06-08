#登録、更新、削除のDB処理、その後の結果画面の呼び出し
from flask import request,redirect,url_for,render_template,flash,session
from holiday import holiday_app,db
from holiday.models.mst_holiday import HolidayMaster
import re


@holiday_app.route('/result.html',methods=['POST'])
def result():
    entries=HolidayMaster.query.all()
    entry_dates=[str(e.holi_date) for e in entries]
    add_date=request.form['holiday']
    add_text=request.form['holiday_text']

    space=add_text.replace('　','')
    space=space.replace(' ','')
    
    if add_date =='':
        flash('日付を入力してください')
        return render_template('input.html')
    elif len(add_date.split('-')[0]) != 4:
        flash('有効な日付を入力してください')
        return render_template('input.html')

    holiday_entry=HolidayMaster(
        date=add_date,
        text=add_text
    )
    if request.form["button"]=="insert_update":
        if space == ''  :
            flash('テキストが空白です。入力してください。')
            return render_template('input.html')
        else:
                
            if add_date in entry_dates:
                
                upd_sub=HolidayMaster.query.get(add_date)
                upd_sub.holi_text=add_text
                db.session.merge(upd_sub)
                db.session.commit()

                print_str=f"{add_date}は「{add_text}」に更新されました"
                return render_template('result.html',print_str=print_str)
            else:
                db.session.add(holiday_entry)
                db.session.commit()
            
                print_str=f"{add_date}は「{add_text}」が登録されました"
                return render_template('result.html',print_str=print_str)
        
    elif request.form["button"]=="delete":
        if add_date in entry_dates:
            
            del_sub=HolidayMaster.query.get(add_date)
            del_sub_text=del_sub.holi_text
            db.session.delete(del_sub)
            db.session.commit()

            print_str=f"{add_date}（{del_sub_text}）は、削除されました"
            return render_template('result.html',print_str=print_str)
        else:
            flash(f'{add_date}は、祝日マスタに登録されていません')
            return render_template('input.html')

