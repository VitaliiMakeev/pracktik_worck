

class Cell:
    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, other):
        return int(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return int(self.cells - other.cells)
        elif other.cells > self.cells:
            return int(other.cells - self.cells)
        else:
            return 'Разность 2 клеток должна быть больше 0'

    def __mul__(self, other):
        cell_result = Cell(self.cells * other.cells)
        return cell_result

    def __str__(self):
        return str(self.cells)

    def __floordiv__(self, other):
        if self.cells > other.cells:
            cell_result_1 = Cell(self.cells // other.cells)
            return cell_result_1
        elif other.cells > self.cells:
            cell_result_1 = Cell(other.cells // self.cells)
            return cell_result_1

    def __truediv__(self, other):
        if self.cells > other.cells:
            cell_result_1 = Cell(self.cells / other.cells)
            return cell_result_1
        elif other.cells > self.cells:
            cell_result_1 = Cell(other.cells / self.cells)
            return cell_result_1

    def make_order(self, cell_row):
        self.cell_row = cell_row
        i = cell_row
        n = r'\n'
        row = ''
        while i <= self.cells:
            rft = cell_row * '*'
            row += f'{rft}{n}'
            i += cell_row
        counter = row.count('*')
        if counter < self.cells:
            bb = str((self.cells % cell_row) * '*')
            return f'{row}{bb}'
        else:
            return row

c1 = Cell(25)
c2 = Cell(30)
dd = c1 / c2
print(type(dd))
print(dd)
c3 = Cell(12)
print(Cell.make_order(c3, 5))