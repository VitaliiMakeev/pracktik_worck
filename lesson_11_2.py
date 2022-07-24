

class ErrorZiro(Exception):
    def __init__(self, messeg='Нельзя делить на ноль!'):
        self.messeg = messeg

    def __str__(self):
        return self.messeg


def division(a, b):
    if a <= 0:
        raise ErrorZiro
    elif b <= 0:
        raise ErrorZiro
    return a / b

try:
    print(division(0, 6))
except ErrorZiro as err:
    print(err)

# try:
#     number_1 = int(input('Введите число делитель: '))
#     if number_1 <= 0:
#         raise ErrorZiro()
# except ValueError:
#     print('Вы ввели не число')
# except ErrorZiro as err:
#     print(err)
# else:
#     print(f'Все нормельно, делим 1000 на {number_1}:', 1000 / number_1)
