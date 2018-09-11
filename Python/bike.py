class bike:
    def __init__(self, price, max_speed,miles): 
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        self.riding = False
        self.count = 0
    def displayinfo(self):
        print(self.price) 
        print(self.max_speed) 
        print(self.miles)
        return self
    def ride(self):
        self.riding = True
        self.count = self.count+ 10
        print(self.count)
        return self
    def reverse(self):
        self.riding = True
        self.count = self.count-10
        print(count)
        return self

bikea = bike(1,2,3)
bikea.displayinfo()