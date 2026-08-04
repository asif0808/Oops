class A:
    def show(self):
        print('from A show')
class B(A):
    def show(self):
        print('from B show')
obj=[B(),A()]
for a in obj:
    a.show()

        