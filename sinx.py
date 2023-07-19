import math

def sinseries(degrees,terms):
    sum=0
    
    for i in range(terms):
        sign = -1**i
        pi = math.pi
        degval = degrees*pi/180
        sum = sum + sign*(degval**(2*i+1)/math.factorial(2*i+1))
        
    return sum

print(sinseries(90,5))