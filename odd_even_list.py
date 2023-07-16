n = int(input("Enter the number of integers: "))

# initialize empty lists for odd and even numbers
odd_numbers = []
even_numbers = []

# read n integers into a list
numbers = []
for i in range(n):
    num = int(input("Enter integer #" + str(i+1) + ": "))
    numbers.append(num)

# separate odd and even numbers into different lists
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# print the two lists
print("Odd numbers: ", odd_numbers)
print("Even numbers: ", even_numbers)