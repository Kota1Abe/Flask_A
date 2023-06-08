from salary_contents import app
from flask import request,redirect,url_for,render_template,flash,session
from salary_contents.calc import calc_salary
@app.route('/')
def show_entries():
    return render_template('input.html',initial_value='')

@app.route('/output.html',methods=['GET','POST'])
def output():
    input_salary=request.form['salary']
    if input_salary == '':
        flash('給与が未入力です。入力してください。')
    elif len(input_salary) > 10 :
        flash('給与には最大9,999,999,999まで入力可能です。')
    elif int(input_salary) < 0 :
        flash('給与にはマイナスの値は入力できません。')
    else:
        salary=calc_salary(input_salary)
        return render_template('output.html',salary=salary)
    return render_template('input.html',initial_value=input_salary)

@app.route('/input.html')
def input():
    return render_template('input.html',initial_value='')
