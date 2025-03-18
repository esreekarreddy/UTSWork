
class Bank:
    def __init__(self):
        self.starting_balance = float(input(f"Enter starting balance: "))
        print(f"Starting balance is ${self.starting_balance:.2f}")

    def deposit(self):
        amount = float(input("Amount to deposit $"))
        self.starting_balance += amount
        print(f'Amount ${amount:.2f} deposited')

    def withdraw(self):
        amount = float(input("Amount to withdraw $"))
        if (amount <= self.starting_balance):
            self.starting_balance -= amount
            print(f'Amount ${amount:.2f} withdrawn')
        else:
            print("Insufficient funds!")

    def show(self):
        print("Current balance is ", self.starting_balance)

    def menu(self):
        operation = input("Start banking (d/w/s/x): ").strip()

        while (operation!="x"):
            match operation:
                case "d":
                    self.deposit()
                case "w":
                    self.withdraw()
                case "s":
                    self.show()
                case _:
                    print("Available options are (d/w/s/x).")

            operation = input("Continue banking. Select operation from (d/w/s/x): ").strip()

    def main(self):
        self.menu()


myBank = Bank()
myBank.main()