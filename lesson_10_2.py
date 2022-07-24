from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def exprensess(self, v=None, h=None):
        self.h = h
        self.v = v
        pass


class Coat(Clothes):

    @property
    def exprensess(self):
        if self.v:
            return (self.v / 6.5) + 0.5



class Suit(Clothes):

    def exprensess(self):
        if self.h:
            f = self.h * 2 + 0.3
            return f


m1 = Coat()
m1.v = 186.3
print(m1.exprensess)
m2 = Suit()
m2.h = 54
print(m2.exprensess())