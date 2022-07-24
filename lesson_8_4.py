

def val_checker(func_1):
    def valll_1(func):
        def wrapper(argv):
            if func_1(argv) == True:
                print(func(argv))
            else:
                msg = f'wrong val {argv}'
                raise ValueError(msg)
        return wrapper
    return valll_1



@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(-5)



