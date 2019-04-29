def task_2(string):
    a=string
    a1=list(a)
    b=len(a)
    c=b // 2
    a2=a1[:c]
    a3=a1[c:]
    a4=a3+a2
    y=''.join(a4)
    return y
print (task_2("12345"))