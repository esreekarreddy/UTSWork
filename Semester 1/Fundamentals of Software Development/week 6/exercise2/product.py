class Product:

    def __init__(self, type, price, stock):
        self.price = price
        self.type = type
        self.stock = stock
    
    @classmethod
    def __default_constructor(cls):
        return cls(input('Type: '), float(input('Price: ')), int(input('Stock: ')))
                   
    def is_empty(self):
        return self.stock == 0

    def stocked(self, stock):
        if stock <= 0:
            raise ValueError("Stock amount must be positive")
        self.stock += stock
        return self.cash(stock)
    
    def sold(self, stock):
        if stock <= 0:
            raise ValueError("Stock amount must be positive")
        self.stock -= stock
        return self.cash(stock)
    
    def has(self, stock):
        if stock <= 0:
            return False
        return self.stock >= stock
    
    def cash(self, stock):
        return stock * self.price
    
    def __str__(self) -> str:
        if self.stock > 0:
            return f'{self.type} stock level: {self.stock} at price {self.price}'
        else:
            return f'{self.type} stock level: {self.stock}'