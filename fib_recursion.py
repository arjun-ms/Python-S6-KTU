def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    print("fib: ")
    for i in range(n):
        print(fib(i))