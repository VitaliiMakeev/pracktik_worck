

matrix_1 = [[2, 3], [5, 7], [8, 9]]
matrix_2 = [[45, 65, 90], [23, 34, 45], [56, 67, 78]]
matrix_3 = [[-1, 64, -8, 70], [95, 30, 54, 10]]
matrix_4 = [[12, 13], [15, 17], [18, 19]]


class Matrix:

    def __init__(self, param_1: list):
        self.param_1 = param_1

    def __str__(self):
        s = ''
        for i in self.param_1:
            s += str(i).replace('[', '|').replace(']', '|').replace(',', '') + '\n'
        return s

    def __add__(self, other):
        result = []
        if len(self.param_1) == len(other.param_1):
            if len(self.param_1[0]) == len(other.param_1[0]):
                for n in range(len(self.param_1)):
                    line = [x + y for x, y in zip(self.param_1[n], other.param_1[n])]
                    result.append(line)
        return Matrix(result)



matr_1 = Matrix(matrix_1)
# print(matr_1)
matr_2 = Matrix(matrix_4)
print(matr_1 + matr_2)


