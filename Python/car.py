class car:
    def __init__(self, price, speed,fuel,milage): 
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
    def display_all(self):
        if (self.price<10000):
            print(self.price)
            print(self.speed)
            print(self.fuel)
            print(self.milage)
            print(0.12)
        if (self.price>10000):
            print(self.price)
            print(self.speed)
            print(self.fuel)
            print(self.milage)
            print(0.15)

carA =car(1,2,3,4)
carA.display_all()