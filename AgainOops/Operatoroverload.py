class A:
    def __init__(self,first):
        self.first=first
    def __add__(self, other):
        res=self.first-other.first
        return res
a=A(7)
b=A(2)
print(a+b)
