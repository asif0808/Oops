# monkey patching
class A:
    def show(self):
        print('Hello from show')
# for specific object
def new_show():
    print('Hello from updated show')
obj=A()
obj.show=new_show
obj.show()
# for all objects of class
def new_show(self):
    print('Hello from updated show')
A.show=new_show
obj1=A()
obj2=A()
obj1.show()
obj2.show()