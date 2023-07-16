# inp_list = [3,5,2,7,8]
# sub_list = [2,7]

str = "malayalam"

i = 0
j = len(str)-1
while(i<=j):
    if(str[i]!=str[j]):
        print("Not palindrome")
        break

    i = i+1
    j = j-1
else:
    print("Palindrome")