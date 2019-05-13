def compare(a, *args, **kwargs):
    res_compar = []
    res_compar_dict = {}
    for arg in args:
        res_compar.append((str(str(a) == str(arg)), str(type(a) == type(arg))))
    for kwarg in kwargs.keys():
        res_compar_dict[kwarg] = (str(str(a) == str(kwargs[kwarg])), str(type(a) == type(kwargs[kwarg])))
    print(res_compar, res_compar_dict)
