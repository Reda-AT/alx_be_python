class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: $ {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew: $ {self.balance}"
        else:
            return f"Insufficient funds."

    def display_balance(self):
        return f"Current Balance: $ {self.balance}"
    
