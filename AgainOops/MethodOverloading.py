class A:
    def add(self,a,b,c=0):
        if c==0:
            return a+b
        else:
            return a+b+c
a=A()
print(a.add(3,5,10))