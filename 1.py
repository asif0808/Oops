# inheritance
class A:
    def __init__(self):
        print('object created')
    def show(self):
        print('Hello from A')
class B(A):
    def __init__(self):
        super().__init__()
        print('object created B')
    def show(self):
        super().show()
        print('Hello from B')
obj=B()
obj.show()