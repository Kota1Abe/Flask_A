from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db

@app.route('/',methods=['GET','POST'])
def homepage():
     
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))# 로그인 함수를 가르킴 
    # return render_template('input.html') #render함수로 html가르킴
    # 내용을 데이터베이스에 등록해야함. 
    return render_template('input.html')


@app.route('/create',methods=['GET','POST'])   

def create():
    date_input = request.form['date_input']
    date_text = request.form['text_input']
    # print(date_input) # 2023-06-07
    # print(date_text) # haha 
    dt = db.session.query(Holiday).filter_by(holi_date=date_input).first()
    # print(dt) # date:2023-06-07 text:birthday
    if dt is True : # 데이터 베이스에 값이 있다면 ,  
        holiday_date = date_input
        dt.holi_text = request.form['text_input']
        holidate_text = dt.holi_text
    else:
        holiday_date=request.form['date_input']
        holiday_text=request.form['text_input']
        dt = Holiday(
        holi_date=holiday_date,
        holi_text=holiday_text
            )
    db.session.merge(dt) # 데이터베이스에 update 내용을 z는다.
    # add , merge의 차이 
    db.session.commit() # 내용을 커밋한다.
    message = request.form['date_input']+request.form['text_input']+"が登録されました。"
    return render_template('result.html',message=message)

@app.route('/delete',methods=['GET','POST'])

def delete():
    dt=request.form['date_input']
    data_date = db.session.query(Holiday).filter_by(holi_date=dt).delete()
    db.session.commit()
    message = request.form['date_input']+request.form['text_input']+"が削除されました。"
    return render_template('result.html',message=message)
    # 데이터 베이스에서 조건에 맞는 튜플 들고옴 
    
@app.route('/result',methods=['GET','POST'])

def result():
    
    result_db = db.session.query(Holiday).order_by(Holiday.holi_date.desc()).all()
   
    

        
    return render_template('list.html',message=result_db)


#     create = Holiday(
#     holi_date=holiday_date,
#     holi_text=holiday_text
#     )
#     db.session.add(create) # 데이터베이스에 update 내용을 넣는다.
#     db.session.commit() # 내용을 커밋한다.
#     message = request.form['date_input']+request.form['text_input']+"が登録されました。"
#     return render_template('result.html',message=message)

# @app.route('/update',methods=['GET','POST'])


##############################################################
#  message ( html의 message )= message -> 함수 안에서 정해진 것 

# @app.route('/update',methods=['GET','POST'])

# def update():
#     date_input = request.form['date_text']
#     dt = session.query(Holiday).fiter_by(holi_date=date_input)
#     if  date_input == dt : 
    
#         update = Holiday(
            
#         )

# html 파일은 로그인이 되었을 때 표시 
# render_template는 templates 폴더의 주소를 가준으로 html 파일을 불러옴 
 
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']: # cofig 파일의 username과 다르면,
#             flash('ユーザ名が異なります')
#         elif request.form['password'] != app.config['PASSWORD']: 
#             flash('パスワードが異なります')
#         else:
#             session['logged_in'] = True # USERNAME과 일치하면, 
#             flash('ログインしました') # 로그인 성공 
#             return redirect(url_for('show_entries')) # 로그인 성공 시, Show 엔트리 함수로 이동
#     return render_template('login.html') # method가 post가 아닌 , get 이면 login.html 
# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('ログアウトしました')
#     return redirect(url_for('show_entries'))


















# @app.route('/')
# def show_entries():
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#     return render_template('entries/index.html')

# @app.route('/')
# def show_entries():
#     # if not session.get('logged_in'):
#     #     return redirect(url_for('login'))
#     return render_template('input.html') # url_for은 함수의 이름을 넣고,
# # render_template의 함수 안에는 파일의 이름을 넣는다 ! 

# @app.route('/input')
# def input():
#     # if not session.get('logged_in'):
#     #     return redirect(url_for('login'))
#     return render_template('input.html') 

# 즉, render_template 함수에서 파일 경로를 저장할 때, template안의 파일 이름을 저장해야함.

# 기본적으로 render_template 함수는 template이라는 디렉토리 경로를 기준으로작성하기 때문에. 


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']:
#             flash('ユーザ名が異なります')
#         elif request.form['password'] != app.config['PASSWORD']:
#             flash('パスワードが異なります')
#         else:
#             session['logged_in'] = True
#             flash('ログインしました')
#             return redirect(url_for('show_entries'))
#     return render_template('login.html')


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('ログアウトしました')
#     return redirect(url_for('show_entries'))