class Car:
    make = ""
    pos = ""
    
    def __init__(self, make, pos):
        self.make = make
        self.pos = int(pos)
        
    def move(self, pos):
        self.pos = pos
        
    def get_details(self):
        print(f"{self.make} is at position: {self.pos}")

car1 = Car("BMW", 0)
car1.get_details()
car1.move(15)
car1.get_details()

