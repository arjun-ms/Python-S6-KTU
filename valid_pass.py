import re

p = input("Enter a password: ")

while True:
    if len(p)<6:
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[@#$]",p):
        break
    else:
        print("valid password")
        break
