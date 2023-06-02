# 給料計算を行う関数の定義を行うファイル
from decimal import Decimal, ROUND_HALF_UP

def calmethod_salary(salary):   # 給料計算用の関数を定義
    if salary <= 1000000:
        tax = Decimal(str(salary * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
        payment = int(salary) - tax
    else:
        tax = Decimal(str(1000000 * 0.1 + (salary - 1000000) * 0.2)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
        payment = int(salary) - tax
    list_calc = [salary, payment, tax]
    return list_calc
