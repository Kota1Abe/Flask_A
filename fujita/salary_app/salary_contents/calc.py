
def calc_salary(money):
    money=int(money)
    if money > 1000000:
        tax=100000+(money-1000000)*0.2

    else:
        tax=money*0.1

    payment=money-tax

    money_str="{:,}".format(int(money))
    pay_str="{:,}".format(int(payment))
    tax_str="{:,}".format(int(tax))

    return f"給与：{money_str}円の場合、支給額:{pay_str}円、税額:{tax_str}円です"