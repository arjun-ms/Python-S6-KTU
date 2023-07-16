def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial cannot be calculated for negative numbers.")
# elif n == 0:
#     print("Factorial of 0 is 1.")
else:
    print(f"Factorial of {n} is {fact(n)}.")