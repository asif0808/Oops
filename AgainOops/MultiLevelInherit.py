class A:
    def __init__(self):
        print('from class A constructor')
    def show(self):
        print('from class A method')
    def showA(self):
        print('from class A show A method')
class B(A):
    def __init__(self):
        print('from class B constructor')
    def show(self):
        print('from class B method')
    def showB(self):
        print('from class B showB method')
class C(B):
    def showc(self):
        print('from c method')
c=C()
c.show()
c.showA()
c.showB()
c.showc()