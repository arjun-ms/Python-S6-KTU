# Write Python program to create a class called as Complex and implement
# __add__( ) method to add two complex numbers. Display the result by
# overloading the + Operator.

class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def __add__(self,num2):
        sum_real  = self.real + num2.real
        sum_imag = self.imag + num2.imag
        
        result = Complex(sum_real,sum_imag)
        return result
    
    def subtract(self,num2):
        sub_real = self.real - num2.real
        sub_imag = self.imag - num2.imag
        
        return Complex(sub_real,sub_imag)
    
    def multiply(self,num2):
        mul_real = self.real * num2.real - self.imag - num2.imag
        mul_imag = self.real * num2.imag + self.imag * num2.real
        
        return Complex(mul_real,mul_imag)    
    
    def display(self):
        print(f"{self.real} + {self.imag}i")
        
    # def __str__(self) -> str:
    #     return f"{self.real} + {self.imag}i"
        
c1 = Complex(1,2)
c2 = Complex(3,4)

sum = c1+c2
mul = c1.multiply(c2)
sub = c2.subtract(c1)
# print(sum)
sum.display()
sub.display()
mul.display()        