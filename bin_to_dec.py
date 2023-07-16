binString = input("Enter a binary number: ")

dec = 0
exponent = len(binString) - 1

for digit in binString:
    dec += int(digit) * 2 ** exponent
    exponent -= 1

print("Decimal equivalent is:", dec)