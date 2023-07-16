dec = int(input("Enter a decimal number: "))
if dec == 0:
    print(0)
else:
    binString = ""
    while dec > 0:
        rem = dec % 2
        dec = dec // 2
        binString = str(rem) + binString
        
    print("Binary equivalent is:", binString)