class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -=amount
    
    def show_balance(self):
        print("Balance is {}".format(self.balance))

    
if __name__ == '__main__':
    jack = Account("Jack", 0)
    jack.show_balance()

    jack.deposite(1000)
    jack.show_balance()
    jack.withdraw(200)
    jack.show_balance()