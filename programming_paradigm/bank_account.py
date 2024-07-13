class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited: $",self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrew: $",self.balance)
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print("Current Balance: $", self.balance)
    
