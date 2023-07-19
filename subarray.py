
l = input("enter a list: ")
l.strip()
l.split()


s = input("enter a sublist: ")
s.strip()
s.split()

# res = False
# for i in range(len(l)):
#     if l[i:i+len(s)] == s:
#         res = True
#         break
    
# print(res)

if s in l:
    print("True")