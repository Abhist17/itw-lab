# Indexing
import numpy as np

# 1
a = np.arange(12)
print(a)
print(a[7])


# 2
b = np.diag([6, 8, 10])
print(b)
print(b[1][1])


# 3
c = np.array([
    [[10, 11], [12, 13]],
    [[14, 15], [16, 17]]
])
print(c)
print(c[1][0][1])


# 4
array = np.arange(12)
print(array)
print(array[1:12:3])


# 5
array[6:9] = 55
print(array)


# 6
b = np.arange(6)
array[0:6] = b[::-1]
print(array)


# 7
b = np.diag([7, 9, 11])
print(b)
print("*" * 10)
b[1][2:] = 88
print(b
