num = int(input("Enter a num: "))

rev = 0
temp = num
sum_of_digits=0
while temp != 0:
    digit = temp%10
    sum_of_digits += digit
    rev = rev * 10 + digit
    temp //= 10
    
print("Reverse of the number is:", rev)

# Check if the number is a palindrome
if num == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

print("Sum of the digits of the number is:", sum_of_digits)
