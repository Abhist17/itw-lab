import numpy as np

# 1 scalar ops
a = np.arange(5)
print(a)

aPlus = a + 5      # add scalar
print(aPlus)

aSq = a**2         # square
print(aSq)

aHalf = a // 2     # floor div
print(aHalf)


# 2 2D array
a = np.array([[2,4,6],[1,3,5]])
print(a**2)        # power


# 3 list loop
L1 = [5,4,3]
L2 = [1,2,3]
L3 = []
for i in range(len(L1)):
    L3.append(L1[i] - L2[i])
print(L3)


# 4 list comp
L3 = [L1[i] - L2[i] for i in range(len(L1))]
print(L3)


# 5 numpy ops
a = np.array([4,5,6])
b = np.array([1,2,3])
print("sub :", np.subtract(a,b))
print("add :", np.add(a,b))
print("div :", np.divide(a,b))
print("mul :", np.multiply(a,b))


# 6 broadcasting
b = np.ones((2,3))
print(b)

b = b + np.array([1,2,3])
print(b)


# 7 matrices
A = np.diag([2,4,6])
B = np.diag([1,3,5])

print(A)
print(B)

print(A * B)       # elementwise
print(A.dot(B))    # matrix mult


# 8 comparison
a = np.array([1,3,5,7])
b = np.array([1,2,5,8])

print(a == b)      # bool array
print(type(a == b))


# 9 equality
print(np.array_equal(a,b))
print(np.array_equal(a,a))
