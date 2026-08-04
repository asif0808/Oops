class A:
    def __init__(self,name,val):
        self.val=val
        print(self)
        self.name=name
    def show(self):
        print(f"value is {self.val}")
        print(f"name is {self.name}")
obj=A('aasif',69)
obj.show() 
obj2=A('john',55)
obj.show()
