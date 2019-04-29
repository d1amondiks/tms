def task_6(string):
    a=string
    a1=list(a)
    b=a1[::-1]
    c=''.join(a1)
    d=''.join(b)
    return c==d
print (task_6("qw e wq"))