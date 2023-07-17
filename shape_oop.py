# Create an Abstract Base Class called Shape that include abstract methods areaQ 
# - unO circumferenceQ. Then derive two classes Circle and Rectangle from
# the Shape class and implement the area0 and circumference$ methods . Write a
# Python program to implement above concept.

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self,r):
        self.radius = r
        
    def area(self):
        print(f"Area: {3.14*self.radius**2}")
    
    def perimeter(self):
        print(f"Circumference: {2*3.14*self.radius}")    

class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def area(self):
        print(f"Area: {self.a * self.b}")
    
    def perimeter(self):
        print(f"Circumference: {2*self.a + 2*self.b}")    
        
        
c1 = Circle(5)
r1 = Rectangle(2,3)

c1.area()
c1.perimeter()
r1.area()
r1.perimeter()