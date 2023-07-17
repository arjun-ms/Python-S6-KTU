import numpy as np
from numpy.linalg import inv,det
# a = np.array([[1,2,3],[4,5,6]])
# print("Dimension of a:",a.ndim)
# print("Shape of a: ",a.shape)
# print("Size of a: ",a.size)
# print("Datatype  of a: ",a.dtype)
# print("Size of each element in a: ",a.itemsize)

# b = np.arange(10)
# print(b)
# b[0:3] = 100
# print(b)


# a = np.array([1,2,3,4,5])
# b = 2*a
# print(b)

A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B # element wise addition
# print(C)

# transpose
print(A.T)
# or
print(A.transpose())

#invese
D = inv(A)
print(D)

# AxA^-1=I
I = A.dot(D)
print(I)

# Sum of diagonal elements
trace = np.trace(A)
print(trace)

# determinant
d = det(A)
print(d)

nums1 = np.random.randint(100,size=5)
print(nums1)

nums2 = np.random.randint(100,size=(5,3))
print(nums2)

# generate a float between 0 and 1.
print(np.random.rand())

print(np.random.choice([1,2,3]))

x = np.array([1,2,3,4])
np.random.shuffle(x)
print(x)
