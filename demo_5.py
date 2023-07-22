class Fraction:

    def __init__(self, num=1, den=1):
        self.num= num
        self.den = den
        self.simplify()

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __repr__(self):
        return f'Fraction <{self.num}/{self.den}>'

    def __mul__(self, other):
        rez_num = self.num * other.num
        rez_den = self.den * other.den
        return Fraction(rez_num, rez_den)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def simplify(self):
        """ 4/6 == > 2/3 """
        pass



f = Fraction(2,1)
f2 = Fraction(2,3)

print(f)
print(f2)

rr = f * f2 * f

print(rr)
print(repr(rr))