from flask import Flask

app = Flask(__name__)

@app.route('/') # / 슬래쉬로 적으면, 127.0.0.1:5000에 응답이 있었을 때, 

# hello_world 함수의 출력이 실행 된다. 

def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run() # flask 웹 어플리케이션을 실행하고, 웹 브라우저로 접근할 수 있게 하는 역할을 수행. 
    print(__name__)
