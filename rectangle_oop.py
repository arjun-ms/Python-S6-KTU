# Write a Python program to define a class Rectangle with parameters height, width
# and member functions to find area, and perimeter of it.

class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        
    def area(self):
        print(f"Area: {self.height * self.width}")
    
    def perimeter(self):
        print(f"Perimeter: {2*(self.width + self.height)}")
    
r1 = Rectangle(1,2)
r1.area()
r1.perimeter()