def inverter (func):
    def inner(*args):
        list1 = []
        dict = {}
        for arg in args:
            if arg != None:
                if isinstance(arg, (int, float, Decimal)) == True:
                    list1.append(-arg)
                if isinstance(arg, bool) == True:
                    if arg == True:
                        list1.append(False)
                    else:
                        list1.append(True)
                if isinstance(arg, str) == True:
                    list1.append(arg[::-1])
                if isinstance(arg, list) == True:
                    list1.append(arg[::-1])
        print(list1)
        func
    return inner

@inverter
def identity(*args):
    return args