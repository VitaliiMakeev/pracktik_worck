

class ItemError(Exception):
    def __init__(self, messeg='Вы ввели не число!'):
        self.messeg = messeg

    def __str__(self):
        return self.messeg

    @staticmethod
    def chekitem(item, sumlist: list):
        try:
            if item.isdigit():
                sumlist.append(item)
            elif item != 'stop':
                raise ItemError
        except ItemError as err:
            print(err)

tmp_2 = []
while True:
    number = input('Введите число: ')
    if number == 'stop':
        print(tmp_2)
        break
    ItemError.chekitem(number, tmp_2)
# tmp = []
# while True:
#     try:
#         number = input('Введите число: ')
#         if number.isdigit():
#             tmp.append(number)
#         elif number == 'stop':
#             print(tmp)
#             break
#         else:
#             raise ItemError
#     except ItemError as err:
#         print(err)
#     except KeyboardInterrupt:
#         print('Пользователь остановил программу на красной кнопочке')
#         break