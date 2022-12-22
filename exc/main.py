import err as err
import re
import entities as e
import random

bank = e.Bank()

class Menu:
    def printMenu(self):
        print("1. Create a new user")
        print("2. Create a new account")
        print("3. Print all users")
        print("4. Print account for user")
        print("5. Deposit for user")
        print("6. Witdraw for user")
        print("7. Exit")


    def createUser(self, names, EGN):
        if re.search("([A-Z]{1})([a-z]+)(\s)([A-Z]{1})([a-z]+){1}", names) == None:
            raise err.InvalidADataFormat("The names must be in format Ivan Petrov")
        if len(EGN) != 10:
            raise err.InvalidADataFormat("The EGN must be exactly 10 numbers long")
        if EGN.isnumeric() == False:
            raise err.InvalidADataFormat("The EGN must contains only numbers")

        user = e.User(names,EGN)
        bank.users.append(user)

    def createAcc(self, currency, accType, IBAN, user):
        if currency != "BGN" and currency != "EUR" and currency != "USD" and currency != "JPY":
            raise err.InvalidADataFormat("the currency can be only: BGN, EUR, USD or JPY")
        if accType != "CURRENT" and accType != "SAVINGS" and accType != "CREDIT":
            raise err.InvalidADataFormat("the account type can be only: CURRENT, SAVINGS or CREDIT")
        
        newUser = None

        for i in bank.users:
            if i.names == user:   
                newUser = i
        if newUser == None:
            raise err.UserNotFound("This user do not exists")

        account = e.Account(currency, accType, IBAN)
        newUser.accounts.append(account)
    
    def createIBAN(self):
        iban = "IB"
        for i in range(0,10):
            iban += str(random.randint(0,9))
        return iban

    def printAllUSers(self):
        bank.printAll()
    
    def printAcc(self, user):
        for i in bank.users:
            if i.names == user:
                user = i
        if user == None:
            raise err.UserNotFound("This user do not exists")
        for i in user.accounts:
            print(i.printAll())
    
    def deposit(self, user, amount, accountType):
        for i in bank.users:
            if i.names == user:
                user = i
        if user == None:
            raise err.UserNotFound("This user do not exists")
        if amount < 0:
            raise err.InvalidADataFormat("The amount of money must be a positive number")
        
        accounts = user.accounts
        for i in accounts:
            if i.accType == accountType:
                i.balnace += amount
        print(f"Successfully added {amount} money")
    
    def witdraw(self, user, amount, accountType):
        for i in bank.users:
            if i.names == user:
                user = i
        if user == None:
            raise err.UserNotFound("This user do not exists")
        if amount < 0:
            raise err.InvalidADataFormat("The amount of money must be a positive number")


        accounts = user.accounts
        for i in accounts:
            if i.balnace < amount:
                raise err.InvalidADataFormat("Not enough money")
            if i.accType == accountType:
                i.balnace -= amount

        print(f"Successfully witdrawed {amount}")
    def run(self):
       
        while True:  
            self.printMenu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":  
                    names = input("Enter first and last name (in format [FirstName LastName]): ")
                    egn = input("Enter the egn (exact 10 digits long): ")
                    self.createUser(names,egn)               
                elif choice == "2":
                    names = input("Enter first and last name (in format [FirstName LastName]): ")
                    currency = input("Enter currency (can be only BGN, EUR, USD or JPY): ")
                    accType = input("Enter account type (can be only CURRENT, SAVINGS or CREDIT): ")
                    iban = self.createIBAN()
                    self.createAcc(currency, accType, iban, names)
                elif choice == "3":
                    self.printAllUSers()
                elif choice == "4":
                    names = input("Enter first and last name (in format [FirstName LastName]): ")
                    self.printAcc(names)
                elif choice == "5":
                    names = input("Enter first and last name (in format [FirstName LastName]): ")
                    amount = float(input("Enter the amount of money you want to deposite(a positive number): "))
                    accType = input("Enter account type: ")
                    self.deposit(names,amount,accType)
                elif choice == "6":
                    names = input("Enter first and last name (in format [FirstName LastName]): ")
                    amount = float(input("Enter the amount of money you want to deposite(a positive number): "))
                    accType = input("Enter account type: ")
                    self.witdraw(names,amount,accType)
                elif choice == "7":
                    break
                else:
                    raise err.InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()
    

if __name__ == '__main__':
    menu = Menu()
    menu.run()