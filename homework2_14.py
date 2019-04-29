def task_14(string):
    a=string
    len_a=len(a)
    if len_a<1:
        return ("VVedi familiyu")
    a1 = a[0]
    b=a.find(' ')+1
    if b==1:
        return ("VVedi familiyu")
    c=a[b:]
    d=""
    while c[-1]==' ':
        c=c[1:]
        if c[-1]!=" ":
            break
    len_c=0
    for i in c:
       if i!=' ':
          d=d+i
          len_c=len_c+1
    endtext=c[len_c:]
    if len(endtext)!=0:
        while endtext[-1]==' ':
            endtext=endtext[1:]
        if endtext[-1]!=' ':
            return ('Value Error, Vvedite tolko Imya i Familiu')
    fin=a1+'.'+d
    return fin
print (task_14("D RE"))
D.RE