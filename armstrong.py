n = int(input("Enter a number: "))
count =0

# count = len(str(n))
# print(count)
temp=n
temp2 = n
while(n>0):
    count = count+1
    n = n//10

sum=0
while(temp>0):
    rem = temp%10
    sum = sum + rem**count
    temp  = temp//10
    
if (temp2 ==sum):
    print("Armstrong number")
else:
    print("Not an armstrong number")