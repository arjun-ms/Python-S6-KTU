import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
m1 = a.reshape(3,3)
b = np.array([1,2,3,4,5,6,7,8,9])
m2 = b.reshape(3,3)

m = np.add(m1,m2)
trans  = np.transpose(m)
print(m)
print("Transpose")
print(trans)

