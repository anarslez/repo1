class item:
    def __init__(self, price, name,weight,brand): 
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        self.condition = 'new'
    def sell(self):
        self.status = 'sold'
        print(self.status)
        return self
    def addtax(self):
        tax = self.price*0.1
        print(tax)
    def returnitem(self):
        if (self.condition == 'new')
            self.status = 'for sale'
        if (self.condition == 'used')
            self.status = 'for sale'
            self.price = self.price * 0.8
    def displayinfo(self):
        print(self.price) 
        print(self.name)
        print(self.weight)
        print(self.brand)
        print(self.status)
        print(self.condition)
        return self