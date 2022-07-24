

class Data:

    def __init__(self, data: str):
        self.data = data

    @classmethod
    def integ(cls, data, arg):
        if arg == 1:
            return int(data.split('-')[0])
        elif arg == 2:
            return int(data.split('-')[1])
        elif arg == 3:
            return int(data.split('-')[2])
        elif arg == 4:
            return int(data.split('-')[0]), int(data.split('-')[1]), int(data.split('-')[2])
        else:
            return 'В дате всего 3 цифры!'

    @staticmethod
    def filed_arg(param: str):
        a = int(param.split('-')[0])
        b = int(param.split('-')[1])
        c = int(param.split('-')[2])
        pres = ''
        if int(param.split('-')[0]) <= 31:
            pres += f'число - {a}, '
        elif a > 31:
            return 'дни месяца от 1 до 31!!!'
        if b <= 12:
            pres += f'месяц - {b}, год - {c}'
        elif b > 12:
            return 'Всего в году - 12 месяцев!!!'
        return pres




d_1 = Data('12-12-2012')
print(d_1.integ('12-12-2012', 5))
print(d_1.filed_arg('23-12-2012'))