class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        self.get_balance()

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            self.get_balance()
        else:
            print("Insufficient balance")
            self.get_balance()

    def get_balance(self):
        print(f"Current balance: {self.balance}")
    
bank = Bank()
action = ""
while action != "exit":
    action = input("Enter the action to perform (deposit/withdraw/balance/exit): ")
    if action == "deposit":
        bank.deposit()
    elif action == "withdraw":
        bank.withdraw()
    elif action == "balance":
        bank.get_balance()
    elif action == "exit":
        break
    else:
        print("Invalid action")