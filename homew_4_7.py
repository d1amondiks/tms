import hmw_2_module


def calc (a,func,b):
    import hmw_2_module
    if func == '-':
        c=hmw_2_module.minus(a,b)
    elif func=='+':
        c=hmw_2_module.plus(a, b)
    elif func=='/':
        c=hmw_2_module.division(a, b)
    elif func=='*':
        c=hmw_2_module.multiplication(a, b)
    return c