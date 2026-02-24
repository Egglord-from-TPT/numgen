def gen(p):
    from decimal import Decimal, getcontext
    if p=="":
        precision=4 # 3206 characters. Wow.
    else:
        precision=p
    multiplier=100 # pls dont touch this variable
    getcontext().prec=(precision*precision)*multiplier
    b="2."
    for i in range(precision):
        b=b+(str((i/Decimal(b))).replace(".",""))
    return b