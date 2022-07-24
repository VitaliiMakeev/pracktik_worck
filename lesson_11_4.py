#Задания 4, 5, 6


class Warehouse:
    """Это класс - склад всего. Принемает список оргтехники (electrics=True),
    и распределяет по классам. Иначе список всео остального"""
    sampty = []
    equipment_list = []

    def __init__(self, equipment=None, electrics=False):
        self.equipment = electrics
        self.equipment = equipment
        if equipment:
            if electrics:
                for i in equipment:
                    Warehouse.equipment_list.append(i)
                    if 'принтер' in i or 'printer' in i:
                        Printer(printer=i, object=i)
                        Equipment.equipment_dict['printer'] += 1
                    elif 'scaner' in i or 'scanner' in i or 'сканер' in i:
                        Scanner(scanner=i, object=i)
                        Equipment.equipment_dict['scanner'] += 1
                    elif 'xerox' in i or 'ксерокс' in i:
                        Xerox(xerox=i, object=i)
                        Equipment.equipment_dict['xerox'] += 1

            else:
                for i in equipment:
                    Warehouse.sampty.append(i)

    def __str__(self):
        return f'{self.equipment_list}\n{self.sampty}'


class Equipment(Warehouse):
    """Это склад оргтехкини. Словарь equipment_dict покажет остатки на складе.
    Есть функция приема техники - priem_equipment(obj=None, cartridge=False, paper=False, computer=False)
    и отправки техники - shipment(type_teh: str, num: int, direction: str)"""
    electrics = True
    equipment_dict = {'printer': 0, 'scanner': 0, 'xerox': 0}

    def __init__(self):
        super().__init__()

    @staticmethod
    def priem_equipment(obj=None, cartridge=False, paper=False, computer=False):
        """Функция приема техники на склад.
        obj - 'printer', 'scanner', 'xerox',
        остальное - наличие того или иного в принимаемой технике"""
        if obj:
            if cartridge == True and paper == True and computer == True:
                Printer(printer=obj, object=obj)
                Equipment.equipment_dict['printer'] += 1
                Warehouse.equipment_list.append(obj)
            elif cartridge == False and paper == False and computer == True:
                Scanner(scanner=obj, object=obj)
                Equipment.equipment_dict['scanner'] += 1
                Warehouse.equipment_list.append(obj)
            elif cartridge == True and paper == True and computer == False:
                Xerox(xerox=obj, object=obj)
                Equipment.equipment_dict['xerox'] += 1
                Warehouse.equipment_list.append(obj)
            else:
                print('Это не принтер, не сканер и не ксерокс!')
        else:
            print('Что помещаем на склад? и поставте параметры: cartridge, paper, computer')

    @staticmethod
    def shipment(type_teh: str, num: int, direction: str):
        """Функция отправи техники в другие подразделения компании
        type_teh - 'printer', 'scaner', 'xerox',
        num - количество едениц отправляемой техники,
        direction - место назначения"""
        if type_teh == 'printer':
            if num <= len(Printer.printer_list):
                Equipment.equipment_dict[type_teh] -= num
                while num != 0:
                    print(f'Этот принтер: {Printer.printer_list[-1]} уезжает в {direction}')
                    Warehouse.equipment_list.remove(Printer.printer_list[-1])
                    Printer.printer_list.pop(-1)
                    num -= 1
            else:
                print(f"На складе осталось {Equipment.equipment_dict['printer']} принтеров")
        elif type_teh == 'scanner':
            if num <= len(Scanner.scanner_list):
                Equipment.equipment_dict[type_teh] -= num
                while num != 0:
                    print(f'Этот сканер: {Scanner.scanner_list[-1]} уезжает в {direction}')
                    Warehouse.equipment_list.remove(Scanner.scanner_list[-1])
                    Scanner.scanner_list.pop(-1)
                    num -= 1
            else:
                print(f"На складе осталось {Equipment.equipment_dict['scanner']} сканеров")
        elif type_teh == 'xerox':
            if num <= len(Xerox.xerox_list):
                Equipment.equipment_dict[type_teh] -= num
                while num != 0:
                    print(f'Этот ксерокс: {Xerox.xerox_list[-1]} уезжает в {direction}')
                    Warehouse.equipment_list.remove(Xerox.xerox_list[-1])
                    Xerox.xerox_list.pop(-1)
                    num -= 1
            else:
                print(f"На складе осталось {Equipment.equipment_dict['xerox']} ксероксов")
        else:
            print('Этого нет на складе оргтехники!')

    def __str__(self):
        return str(self.equipment_dict)


class Printer(Equipment):
    printer_list = []
    cartridge = True
    paper = True
    computer = True

    def __init__(self, printer=None, object=None):
        self.printer = printer
        self.object = object
        if printer:
            Printer.printer_list.append(printer)
            if object:
                print(object, id(object),)
        super().__init__()

    def __str__(self):
        return f'{self.printer_list}'


class Scanner(Equipment):
    scanner_list = []
    cartridge = False
    paper = False
    computer = True

    def __init__(self, scanner=None, object=None):
        self.scanner = scanner
        self.object = object
        if scanner:
            Scanner.scanner_list.append(str(scanner))
            if object:
                print(object, id(object))
        super().__init__()

    def __str__(self):
        return str(self.scanner_list)


class Xerox(Equipment):
    xerox_list = []
    cartridge = True
    paper = True
    computer = False

    def __init__(self, xerox=None, object=None):
        self.object = object
        self.xerox = xerox
        if xerox:
            Xerox.xerox_list.append(str(xerox))
            if object:
                print(object, id(object))
        super().__init__()

    def __str__(self):
        return str(self.xerox_list)

list_prr_1 = ['принтер_1', 'printer_3', 'xerox_2', 'ксерокс_2', 'scanner_3', 'scaner_4', 'сканер_5']
ddd = Warehouse(list_prr_1, electrics=True)
print(Warehouse.equipment_list)

printer_1 = Equipment()
Equipment.priem_equipment('printer_1', cartridge=True, paper=True, computer=True)

Equipment.priem_equipment('xerox_1', cartridge=True, paper=True)
Equipment.priem_equipment('scanner_1', computer=True)
Equipment.priem_equipment('scanner_2', computer=True)
Equipment.priem_equipment('printer_2', cartridge=True, paper=True, computer=True)
print(Printer.printer_list)
Equipment.shipment('printer', 1, 'Moscow')
print(Equipment.equipment_dict)
print(Xerox.xerox_list)
aaa = Printer()
print(aaa)
bbb = Equipment()
print(bbb)
ccc = Warehouse()
print(ccc)