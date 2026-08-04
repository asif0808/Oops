class A:
    def show(self):
        print('from class A')
class B:
    def show(self):
        print('from class B')
class C(A,B):
    def disp(self):
        print('from c')
c=C()
c.show()