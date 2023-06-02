from flask import request,redirect,url_for,render_template,flash,session
from salary import app
from decimal import Decimal , ROUND_HALF_UP

def calcsalary(salary):
    if salary >= 1000000:
        tax=(salary-1000000)*0.2+100000

    else:
        tax=salary*0.1

    tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    pay_amount=salary-tax
    return pay_amount,tax
        






@app.route('/')
def show_entries():
    return render_template("input.html")
    #return "mikami"
    """
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    return render_template("entries/index.html")
    """

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        salary=int(request.form["salary"])
        pay_amount,tax=calcsalary(salary)

    return render_template("output.html",salary=salary,pay_amount=pay_amount,tax=tax)
    
@app.route("/output",methods=["GET","POST"])
def logout():
    return render_template("input.html")