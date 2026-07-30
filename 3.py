# Encapsulation
# class Bank:
#     def __init__(self,balance):
#         self.__balance=balance
#     def add_balance(self,amount):
#         self.__balance+=amount
#     def get_balance(self):
#         return self.__balance
# user1=Bank(1000)
# print(user1.get_balance())
# user1.add_balance(3000)
# print(user1.get_balance())

class Bank:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount<500:
            raise ValueError('Amount must be greater than equal to 500')
        self.__balance+=amount
user1=Bank(1000)
print(user1.balance)
user1.balance=3000
print(user1.balance)