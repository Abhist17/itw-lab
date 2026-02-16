import numpy as np

# 1 basic reduce
a = np.array([10, -3, 7, 21])
print("a:", a)

print("sum:", np.sum(a))     # sum
print("min:", np.min(a))     # min
print("max:", np.max(a))     # max
print(type(np.sum(a)))       # type


# 2 axis sum
a = np.array([2, 4, 6])
b = np.array([1, 1, 1])

print(np.sum([a, b]))              # total
print(np.sum([a, b], axis=0))      # col sum
print(np.sum([a, b], axis=1))      # row sum


# 3 2D reduce
x = np.array([[2, 1],
              [3, 4],
              [1, 5]])
print(x)
print(x.shape)

print("rsum:", x.sum(axis=1))       # row
print("csum:", x.sum(axis=0))       # col


# 4 mean
x = np.array([2, 4, 6, 8])
y = np.array([[1, 3, 5],
              [2, 4, 6]])

print(x.mean())                     # mean
print(type(x.mean()))

print(y.mean())                     # mean all
print(type(y.mean()))

print(np.mean(y, axis=0))           # col mean
print(type(np.mean(y, axis=0)))

print(np.mean(y, axis=1))           # row mean
print(type(np.mean(y, axis=1)))
