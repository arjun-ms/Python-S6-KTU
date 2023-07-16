class Square:
    def __init__(self,side):
        self.side = side
    
    def area(self):
        print(self.side**2)
    
    def perm(self):
        print(self.side*4) 

first = Square(5)
first.area()
first.perm()