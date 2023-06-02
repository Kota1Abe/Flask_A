from flask import request, redirect, url_for, render_template, flash, session
from salary import app


@app.route('/')
def show_entries():
    return render_template("input.html") # 경로가 / 라면 , input.html 참조 

@app.route('/output', methods=['GET', 'POST']) # 경로가 /output일 때 , get, post 멧고도
def output():
    money = 1000000
    error = None
    if request.method == 'POST':
        salary_int = int(request.form['salary'])
       
        if salary_int>money:

            res = salary_int - money
            zekin = res * 0.2 + money * 0.1 
        
        else:
            zekin = salary_int * 0.1 
            # return redirect(url_for('show_entries')) # 리다이렉트는 실제로, 이동, url for 지정 # def 만 
        
        real=salary_int - zekin 
        real =str(real)
        return render_template('output.html', val=real,ze=zekin) # output에서 급여 계산 결과 출력 , html에 참조 
    
    return redirect(url_for("show_entries")) 
# @app.route("/keisan")

# def 
# # money = 1000000 

# # input_money = 120000

# # if input_money > money: 
    
