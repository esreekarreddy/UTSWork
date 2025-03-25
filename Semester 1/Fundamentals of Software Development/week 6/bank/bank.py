from customer import Customer

class Bank:
    def __init__(self):
        self.customer = Customer("John Smith")
    
    def read_amount(self, action):
        while True:
            try:
                print(f"Amount to {action} $", end='')
                amount = float(input())
                if amount <= 0:
                    print("Amount must be positive. Please try again.")
                    continue
                return amount
            except ValueError:
                print("Please enter a valid number.")

    def deposit(self):
        amount = self.read_amount("deposit")
        if self.customer.deposit(amount):
            print(f'Amount ${amount:.2f} deposited')
        else:
            print("Deposit failed. Please try again.")
    
    def withdraw(self):
        amount = self.read_amount("withdraw")
        if self.customer.is_sufficient(amount):
            if self.customer.withdraw(amount):
                print(f'Amount ${amount:.2f} withdrawn')
            else:
                print("Withdrawal failed. Please try again.")
        else:
            print("Insufficient funds")

    def transfer(self):
        amount = self.read_amount("transfer")
        if self.customer.is_sufficient(amount):
            if self.customer.transfer(amount):
                print(f'Amount ${amount:.2f} transferred to loan account')
            else:
                print("Transfer failed. Please try again.")
        else:
            print("Insufficient funds")
    
    def show(self):
        self.customer.show()
    
    def read_choice(self):
        return input("Start Banking (d/w/t/s/x): ")

    def help(self):
        print("\nAvailable Commands:")
        print("d - deposit money to savings account")
        print("w - withdraw money from savings account")
        print("t - transfer money from savings to loan account")
        print("s - show account details")
        print("x - exit")
        print()
    
    def main(self):
        print("Welcome to the Banking System")
        self.help()
        choice = self.read_choice()

        while choice != 'x':
            match choice:
                case 'd':
                    self.deposit()
                case 'w':
                    self.withdraw()
                case 't':
                    self.transfer()
                case 's':
                    self.show()
                case _:
                    self.help()
            choice = self.read_choice()
        print("Thank you for banking with us!")
    
    def __str__(self) -> str:
        return f'Banking for {self.customer}'

if __name__ == '__main__':
    bank = Bank()
    bank.main()