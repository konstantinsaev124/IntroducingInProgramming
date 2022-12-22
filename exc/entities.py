class Bank():
    def __init__(self):
        self.users = []

    def printAll(self):
        for i in self.users:
            print(f"{i.printAll()}")
        

class User():
    def __init__(self, names, EGN):
        self.names = names
        self.accounts = []
        self.EGN = EGN
    
    def printAll(self):
     
        print(f"{self.names} with EGN: {self.EGN} and accounts")
        for i in self.accounts:
            print(i.printAll())

class Account():
    def __init__(self, currency, accType, IBAN):
        self.balnace = 0
        self.currency = currency
        self.accType = accType
        self.IBAN = IBAN
    
    def printAll(self):
        return f"balance: {self.balnace}{self.currency}. Account type: {self.accType} with IBAN: {self.IBAN}"