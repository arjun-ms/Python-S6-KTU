n = int(input("Enter a num: "))

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

if is_prime(n):
    print("Prime")
else:
    print("Not prime")