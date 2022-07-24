

class Stationery:
    title: str = 'название'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки маркером'


fun_1 = Stationery()
print(fun_1.draw())
print(fun_1.title)
fun_2 = Pen()
print(fun_2.draw())
fun_3 = Pencil()
print(fun_3.draw())
fun_4 = Handle()
print(fun_4.draw())