class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: $ {amount}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient funds."
        elif self.balance >= amount:
            self.balance -= amount
            return f"Withdrew: $ {amount}"

    def display_balance(self):
        return f"Current Balance: $ {self.balance}"
    
