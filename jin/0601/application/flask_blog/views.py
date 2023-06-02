# from flask import request,redirect,url_for, render_template,flash,session

# from flask_blog import app 


# @app.route("/")

# def show_entries():
#     if not session.get("logged_in"): # 로그인 안되었을 때 
#         return redirect("/login") # 로그인 하는 창으로 가게한다. 

#     return render_template("entries/index.html")

# @app.route("/login" , methods = ["GET","POST"]) # 로그인 할때 , 아이디와 비번을 받고, 


#                     #  <a class =" nav-link" href ="/login"> ログイン </a > HTML의 여기로 연결됨 

# # get메서드는 사용자가 웹 페이지에서 정보를 요청할 때 사용 

# def login():
#     if request.method == "POST": # 만약 사용자로부터 입력을 받았다면 , 
#         if request.form["username"] != app.config["USERNAME"]: # 유저 네임에 저장되어 있는 사용자의 이름과 비교 
#             flash("ユーザー名が異なります。")
#         elif request.form["password"]!=app.config["PASSWORD"]: # 패스워드 비교 
#             flash("パスワードが異なります。")
#         else:
#             session["logged_in"]=True # 세션의 로그인 키가 TRUE로 된다. 


#             flash("ログインしました")
              
#     return render_template("login.html")


# @app.route("/logout")
# def lougout():
#     session.pop("logged_in",None)
#     return redirect("/")




# sever -> init -> views -> index.html 

##########################################################################################################

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))