class Fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    def __str__(self):
        return f'{self.num}/{self.den}'
    def __add__(self, other):
        num=(self.num*other.den)+(other.num*self.den)
        den=self.den*other.den
        return f'{num}/{den}'
    def __sub__(self, other):
        num=(self.num*other.den)-(other.num*self.den)
        den=self.den*other.den
        return f'{num}/{den}'
    def __mul__(self, other):
        num=self.num*other.num
        den=self.den*other.den
        return f'{num}/{den}'
    def __truediv__(self, other):
        num=self.num*other.den
        den=self.den*other.num
        return f'{num}/{den}'
         
d1=Fraction(4,5)
print(d1)
d2=Fraction(9,3)
print(d2)
print(d1+d2)
print(d1-d2)
print(d1*d2)
print(d1/d2)
