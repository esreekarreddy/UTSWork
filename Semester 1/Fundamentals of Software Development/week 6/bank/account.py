class Account:
    def __init__(self, account_type):
        self.type = account_type
        self.balance = self.read_balance()

    def read_balance(self):
        while True:
            try:
                print(f'Initial {self.type} balance $', end='')
                balance = float(input())
                if balance < 0 and self.type == "Savings":
                    print("Savings account cannot have negative balance. Please enter a positive value.")
                    continue
                return balance
            except ValueError:
                print("Please enter a valid number.")
    
    def has_balance(self, amount):
        return self.balance >= amount
    
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            return False
        self.balance -= amount
        return True

    def pay_to(self, amount, target):
        if amount <= 0:
            return False
        self.balance -= amount
        target.balance += amount
        return True
    
    def __str__(self):
        return f'{self.type} balance: ${self.balance:.2f}'
