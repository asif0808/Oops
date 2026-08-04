class Bank:
    def __init__(self,amount):
        print('Account created')
        self.__bal=amount
    def deposit(self,amount):
        self.__bal+=amount
    def debit(self,amount):
        self.__bal-=amount
    def get_bal(self):
        return self.__bal
user1=Bank(1000)
print(user1.get_bal())
user1.deposit(2000)
print(user1.get_bal())
user1.debit(3000)
print(user1.get_bal())