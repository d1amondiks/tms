from decimal import Decimal

def return_invert(arg):          #make invert coming element
    if isinstance(arg, (int, float, Decimal)) == True and isinstance(arg, bool) == False:
        arg = -arg
    if isinstance(arg, bool) == True:
        arg = not arg
    if isinstance(arg, str) == True:
        arg = arg[::-1]
    if isinstance(arg, list) == True:
        arg = arg[::-1]
    return arg

def invert(*args):               #invert all coming functions
    list1=[]
    for arg in args:
        list1.append(return_invert(arg))
    return list1

def inverter (func):             # decorator
    def inner(*args,**kwargs):
        list2=[]
        for arg in args:
            list2.append(return_invert(arg))
        print(list2)
        dic={}
        dic_fin={}
        dic.update(kwargs)
        print(dic)
        sort_dic=sorted(dic)
        print sort_dic
        for i in range(5):
            dic_fin[return_invert(sort_dic[i])]=dic[sort_dic[i]]
        return func(*list2[:5],**dic_fin)
    return inner

@inverter
def identity(*args,**kwargs):
    return args, kwargs
