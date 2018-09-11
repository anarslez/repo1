class animal:
    def __init__(self, health, name): 
        self.health = health
        self.name = name
        self.handi = handi
    def walk(self):
        self.health = self.health-self.handi
        print(self.health)
        return self
    def run(self):
        self.health = self.health-5
        print(self.health)
        return self   
class dog(animal):
    def __init__(self, name):
        super().__init__(150,name)
    def pet(self):
        self.health = self.health+5
        print(health)
        return self
class dragon(animal):
    def __init__(self, name):
        super().__init__(170,name)
    def fly(self):
        self.health = self.health+5
        print(self.health)
        print('i am a dragon')
        return self
