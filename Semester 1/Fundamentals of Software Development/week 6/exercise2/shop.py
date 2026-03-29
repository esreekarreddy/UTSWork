from product import Product
from cashregister import CashRegister

class Shop:
    def __init__(self):
        self.product = Product('Cap', 10, 7)
        self.register = CashRegister()

    def sell(self):
        stock = int(input('Stock: '))
        if stock <= 0:
            print('Invalid quantity')
            return
        cash = self.product.cash(stock)

        if self.product.has(stock):
            self.register.gain(cash)
            self.product.sold(stock)
            print(f'Sold {stock} {self.product.type}(s) for ${cash:.2f}')
        else:
            print(f'Not enough stock')
    
    def restock(self):
        stock = int(input('Stock: '))
        if stock <= 0:
            print('Invalid quantity')
            return
        cash = self.product.cash(stock)

        if self.register.has(cash):
            self.register.pay(cash)
            self.product.stocked(stock)
            print(f'Restocked {stock} {self.product.type}(s) for ${cash:.2f}')
        else:
            print(f'Not enough funds')

    def view(self):
        print(self.product)
        print(self.register)
    
    def help(self):
        print('s - sell')
        print('r - restock')
        print('v - view')
        print('x - exit')

    def menu(self):
        choice = input('Choice Sell(s), Restock(r), View(v), Exit(x): ')
        while choice != 'x':
            match(choice):
                case 's': self.sell()
                case 'r': self.restock()
                case 'v': self.view()
                case _: self.help()
            choice = input('Choice Sell(s), Restock(r), View(v), Exit(x): ')
    
def main():
    shop = Shop()
    shop.menu() 

if __name__ == '__main__':
    main()