class Md:
    def __init__(self):
        self.start = 0
    def add(self,*nums):
        for i in nums:
            self.start = self.start + i
        return self
    def sub(self,*subs):
        for i in subs:
            self.start = self.start - i
        return self
    def result(self):
        print(self.start)
    
md = Md()
md.add(1,2,3,3).sub(1,3,3).result()
