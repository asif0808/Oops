# decorator
def Modification_func(func):
    def inner():
        print('Greetings...')
        func()
        print('Program ends')
    return inner
@Modification_func
def Existing_func():
    print(f'Hello Aasif, Good Morning')
Existing_func()

# decorator with argument
def Outer(args):
    def Modification(func):
        def inner(*args,**kwargs):
            print('Before exisiting fun')
            func(*args,**kwargs)
        return inner
    return Modification
def Existing(name):
    print(f'Hello {name}, Good Morning')

Existing('John')