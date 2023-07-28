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
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        rez_num = self.num * other.den
        rez_den = self.den * other.num
        return Fraction(rez_num, rez_den)

    def simplify(self):
        """ 4/6 == > 2/3 """
        n = min(abs(self.den), abs(self.num))
        while n > 1:
            if self.den % n == 0 and self.num % n == 0:
                self.num = self.num // n
                self.den = self.den // n
                break
            n -= 1


f = Fraction(2,1)
f2 = Fraction(2,3)

print(f)
print(f2)

rr = f * f2 * f

print(rr)
print(f + f2)
# print(repr(rr))

print(Fraction(10, 45))
print(f2 / Fraction(10, 45))
