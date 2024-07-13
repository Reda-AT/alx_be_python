class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: $ {amount}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew: $ {amount}"
        else:
            return f"Insufficient funds."

    def display(self):
        return f"Current Balance: $ {self.balance}"
    
