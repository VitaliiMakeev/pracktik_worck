

def type_loger(func):
    name = func.__name__
    def wrapper(*args):
        tmp = []
        for n in args:
            str_1 = f'{name}({n}: {type(func(n))})'
            tmp.append(str_1)
        print(str(tmp).replace('"', '').replace('[', '').replace(']', ''))
    return wrapper


@type_loger
def calc_cube(*args):
    for i in args:
        return i ** 3


a = calc_cube(5)
calc_cube(5, 6, 8, 7)