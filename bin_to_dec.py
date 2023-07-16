binString = input("Enter a binary number: ")
dec=0
exponent = len(binString)-1
for ch in binString:
    dec += int(ch) * 2 ** exponent
    exponent -= 1
    
print("Decimal equivalent of", binString, "is", dec)