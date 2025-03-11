class Bank:
    current_balance = 1000

    def main(self):
        print("Balance at the start is: ", self.current_balance)
        operation = input("Start banking (d/w/s/x): ").strip()

        while operation != "x":
            match operation:
                case "d":
                    deposit_amount = float(input("Amount to deposit: "))
                    self.current_balance += deposit_amount
                    print(f'Amount ${deposit_amount:.2f} deposited')
                case "w":
                    withdraw_amount = float(input("Amount to withdraw: "))
                    if withdraw_amount <= self.current_balance:
                        self.current_balance -= withdraw_amount
                        print(f'Amount ${withdraw_amount:.2f} withdrawn')
                    else:
                        print("Insufficient funds!")
                case "s":
                    print("Current balance is ", self.current_balance)
                case _: 
                    print("Available options (d/w/s/x).")
                    
            operation = input("Continue banking (d/w/s/x): ").strip()


if __name__ == "__main__":
    my_bank = Bank()
    my_bank.main()