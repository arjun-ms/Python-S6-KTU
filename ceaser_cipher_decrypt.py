code = input("Enter the coded text: ")
dist = int(input("Enter the distance: "))
msg = ""

for ch in code:
    ordvalue = ord(ch)
    cipherval = ordvalue - dist
    
    if cipherval < ord('a'):
        cipherval = ord('z') - dist + (ordvalue - ord('a') + 1)
    
    msg += chr(cipherval)

print(msg)