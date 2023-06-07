from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from functools import wraps



@app.route('/')
def show_result():
    return render_template('index.html')

@app.route('output',methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        try:
            if int(request.form['salary']) != None:
                flash('数値が入力されました')
                sla = calc_salary(int(request.form['salary']))
                return  redirect(url_for('output',sla[0],sla[1],sla[2]))
        except:
            pass
    return render_template('input.html')
                


def calc_salary(salary):
    if salary >= 10000000:
        tax = 10000000 * 0.1 + (salary - 10000000) * 0.2
    else:
        tax = salary * 0.1
    return [salary, salary-tax, tax]
    