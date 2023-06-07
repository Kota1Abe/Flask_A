from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from functools import wraps



@app.route('/')
def show_result():
    return render_template('index.html')

@app.route('/output',methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        try:
            num = int(request.form['salary']) 
            flash('数値が入力されました')
            sla = calc_salary(num)
            return  render_template('/output.html', sla=sla)
        except:
            flash('数値以外が入力されました')
            pass
    return render_template('/index.html')


def calc_salary(salary):
    if salary >= 10000000:
        tax = 10000000 * 0.1 + (salary - 10000000) * 0.2
    else:
        tax = salary * 0.1
    sal = [salary, salary-tax, tax]
    return sal
    