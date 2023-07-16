msg = input("enter a word: ")
dist = int(input("enter a distance: "))
code = ""


for ch in msg:
    # represents integer value of a letter
    ordvalue = ord(ch)
    ciphervalue = ordvalue + dist
    
    if ciphervalue > ord('z'):
        # If the cipher value goes beyond 'z', wrap around to 'a'
        # by subtracting the difference between the cipher value and 'z' 
        # from the shift distance, and adding the result to the ASCII value of 'a'
        ciphervalue = ord('a') + dist - (ord('z') - ordvalue + 1)
        
    code += chr(ciphervalue)

print(code)
