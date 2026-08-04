class Parent:
    def __init__(self):
        print('Parent class constructor')
    def show(self):
        print('from parent show')
class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Child class constructor')
    def show(self):
        super().show()
        print('child show')
c=Child()
c.show()