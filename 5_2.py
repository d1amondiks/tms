from decimal import Decimal

count_notevent=lambda x: (x%2==0 and x%10!=0 and 0<=x<=100)
count_result=lambda x: (x*2 if x%2!=0 else x/2)
count_plus_dec=lambda x:x if x>0 else 0

def task_2_a (*args):
    print(list(filter(count_notevent ,args)))

def task_2_b(*args):
    print(list(map(count_result, args)))

def task_2_d(*args):
    sum = Decimal(0)
    count = Decimal(0)
    for arg in args:
        if count_plus_dec(arg) != 0:
            sum += count_plus_dec(arg)
            count += 1
    sr_arif_posit = sum / count if count > 0 else 0
    print(sr_arif_posit)
