#Ploymorphism
class A:
    def show(self):
        print('Show from A')
class B:
    def show(self):
        print('show from B')

objs=[A(),B()]
for obj in objs:
    obj.show()