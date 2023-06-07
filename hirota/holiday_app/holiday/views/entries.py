from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Entry


@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.holi_date.desc()).all()
    return render_template('/list.html', entries=entries)


@app.route('/input', methods=['POST'])
def merge_entry():
    holi_date=request.form['holi_date']
    holi_text=request.form['holi_text']
    text = f"{holi_date}({holi_text})が登録されました"
    entry = Entry(
            holi_date=request.form['holi_date'],
            holi_text=request.form['holi_text']
            )
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return render_template('/result.html', text2=text)
    # return redirect(url_for('result_entry', text=text))



@app.route('/input', methods=['GET'])
def input_entry():
    return render_template('/input.html')

@app.route('/delete', methods=['POST'])
def delete_entry():
    try:
        holi_date = request.form["holi_date"]
        entry = Entry.query.get(holi_date)
        holi_text = entry.holi_text
        db.session.delete(entry)
        db.session.commit()
        text = f'{holi_date}({holi_text})は、削除されました'
        flash(f'{holi_date}({holi_text})は、削除されました')
        return render_template('/result.html', text2=text)
        # return redirect(url_for('result_entry', text=text))
    except:
        holi_date = request.form["holi_date"]
        text = f'{holi_date}は、祝日マスタに登録されていません。'
        flash(text)
        return render_template('/input.html')

# @app.route('/result', methods=['GET'], )
# def result_entry(text2):
#     text2 = text2
#     return render_template('/result.html', text2=text2)