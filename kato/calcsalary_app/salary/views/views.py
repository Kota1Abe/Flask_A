from flask import request, redirect, url_for, render_template, flash, session
from salary import app
import salary.calc_salary

@app.route('/', methods=['GET', 'POST'])
def show_entries():
    return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method=='POST':
        if request.form['salary'] == None:
            flash('給料が入力されていません')
        else:
            session['salary'] = True
            salary = int(request.form['salary'])
            flash('給料を計算します')
            [salary, payment, tax] = salary.calc_salary.calmethod_salary(salary)
            return redirect(url_for('output', salary, payment, tax))
    return render_template('input.html')
