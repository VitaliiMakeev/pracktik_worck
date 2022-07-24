

class Complex_number:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __mul__(self, other):
        return self.a * other.a

number_1 = Complex_number(5)
number_2 = Complex_number(4)
print(number_1 + number_2)
print(number_1 * number_2)