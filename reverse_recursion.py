def reverse(n):
    if n<10:
        print(n,end="")
    else:
        print(n%10,end="")
        return reverse(n//10)
# Read number
number = int(input("Enter number: "))
# Function call
reverse(number)

