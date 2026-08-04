class A:
    def show(self):
        print('show from A')
class B(A):
    def show(self):
        print('show from B')
class C(B):
    pass
c=C()
c.show()
# A().show()