# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name} is barking.")

#     def dog_info(self):
#         print(f"dog name: {self.name}\ndog age: {self.age}")

# dog1 = Dog("Doglas", 3)
# dog2 = Dog("Mark", 19)

# print(dog1.name)
# print(dog1.age)
# dog1.bark()

# print("---------")
# print(dog2.name)
# print(dog2.age)
# dog2.bark()

class BankAccountPublic:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        amount = int(input("How much do you want to deposit? "))
        self.balance += amount

    def withdraw(self, amount):
        amount = int(input("How much do you want to withdraw? "))
        self.balance -= amount

class BankAccountPrivate:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        amount = int(input("How much do you want to deposit? "))
        self.__balance += amount

    def withdraw(self, amount):
        amount = int(input("How much do you want to withdraw? "))
        self.__balance -= amount

account1 = BankAccountPrivate(1000)
account2 = BankAccountPublic(1000)

account1.balance = 9999999
account1.__balance = 9999999
account2.balance = 9999999

print("")
print(account1.get_balance())
print(account2.get_balance())
print("")