

class Worker:
    name: str = 'Виталий'
    surname: str = 'Макеев'
    position: str = 'Слесарь по вентиляции'
    _income: dict = {'wage': 15000, 'bonus': 12000}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'


    def get_total_income(self):
        income = self._income['wage'] + self._income['bonus']
        return f'Доход сотрудника: {income}'

worker_1 = Position()
worker_1.name = 'Виктор'
print(worker_1.get_full_name())
print(worker_1.get_total_income())

