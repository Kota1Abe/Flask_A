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
    entry = Entry(
            holi_date=request.form['holi_date'],
            holi_text=request.form['holi_text']
            )
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/input', methods=['GET'])
def new_entry():
    return render_template('/input.html')

@app.route('/list', methods=['GET'])
def show_entry(holi_date):
    entry = Entry.query.get(holi_date)
    return render_template('result.html', entry=entry)



@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(holi_date):
    entry = Entry.query.get(holi_date)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))