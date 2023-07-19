# birthdays = {
#     "John": "1990-05-20",
#     "Alice": "1985-11-10",
#     "Bob": "1995-08-15",
#     "Eve": "1992-04-30"
# }

# # for key in birthdays:
# #     print(key)

# # print(list(birthdays.items()))

# thisset = {"apple", "banana", "cherry"}
# thisset.update([1,2,3,3])
# print(thisset)

# import random 

# a = random.randint(1,3)
# print(a)

# import os
# filepath="code.txt"
# if os.path.exists(filepath):
#     with open(filepath,'w') as f:
#         print("file opened successfully")
# else:
#     print("File doesn't exists")

# import numpy as np
# arr = np.array([[1,2,3],
#        [4,5,6],
#        [7,8,9]])

# print(arr[:2])
# print(arr[:2,1:])
# print(arr[1,:2])
# arr[:2,1:]=0
# print(arr)

# a = [1,2,3,4]
# g= 3
# for item in a:
#        if item ==g:
#               print(a.index(g))

# first = [1, 2, 3, 5]
# second = [2, 4, 5, 7]
# common = [x for x in first if x in second]
# print(common)

# str = "abdavdvadvfsd"
# freq = {}
# for letter in str:
#        freq[letter] = freq.get(letter,0) + 1

# print(freq)
# freq.clear()
# print(freq)

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.update({"color": "White"})
# # car['color'] = "Blue"

# print(car)

# import os
# for dirpath, dirnames, filenames in os.walk('/home/ams/Documents/python-s6/'):
#     print(f"Current Directory: {dirpath}")
#     print(f"Subdirectories: {dirnames}")
#     print(f"Files: {filenames}\n")

# class moverload:
#        def display(self,a=None,b=None):
#               print(a,b)
              
# obj=moverload()
# obj.display()
# obj.display(10)
# obj.display(10,20)

# import pandas as pd
# data = {
# "calories": [420, 380, 390],
# "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index=["D1","D2","D3"])
# print(df)
# print(df.loc["D1"])
# import numpy as np
# a = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(a == 4)
# print(x)
# a.sort()
# print(a)

# import matplotlib.pyplot as plt
# import numpy as np
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1,2,1)
# plt.plot(x,y)
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1,2,2)
# plt.plot(x,y)
# plt.show()