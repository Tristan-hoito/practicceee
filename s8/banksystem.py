class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        print("")
        print(f"Your total amount is {self.__balance}")
        print("Thank you for using our Bank!")
        return
    
    def deposit(self):
        amount = int(input("How much do you want to deposit? "))
        self.__balance += amount
        print("")
        print(f"Your now total amount is {self.__balance}")
        print("Thank you for using our Bank!")
        print("")
        return

    def withdraw(self):
        amount = int(input("How much do you want to withdraw? "))

        if amount > self.__balance:
            print("")
            print("You do not have enough money.")
            print("")
            return
        
        else:
            self.__balance -= amount
            print("")
            print(f"Your now total amount is {self.__balance}")
            print("Thank you for using our Bank!")
            return

account1 = BankAccount(1000)

def banksystem():
    while True:
        print("")
        print("Welcome to PyBankAccount System!")
        print("")
        print("[1] Check your Balance")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Exit")
        print("")

        try:
            choice = int(input("Please choose a function from 1-4: "))

            match choice:
                case 1:
                    account1.get_balance()

                case 2:
                    account1.deposit()
                
                case 3:
                    account1.withdraw()

                case 4:
                    print("")
                    print("Exiting.....")
                    print("")
                    exit()
        
        except ValueError:
                print("")
                print("Please choose from 1-4 only.")
                print("")

banksystem()