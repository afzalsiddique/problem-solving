class Laptop:
    def __init__(self,ram,ssd):
        self.ram=ram
        self.ssd=ssd
    def __lt__(self, other):
        if self.ram!=other.ram:
            return self.ram-other.ram
        return self.ssd-other.ssd
    def __eq__(self, other):
        return True if self.ram==other.ram and self.ssd==other.ssd else False
    def __repr__(self): return str([self.ram, self.ssd])

li = [Laptop(16,128),Laptop(8,512),Laptop(8,256)]
li.sort()
print(li)
x = Laptop(16,128)==Laptop(16,128)
print(x)
