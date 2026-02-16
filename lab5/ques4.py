import numpy as np

# 1 load data
idata = np.loadtxt('populations.txt')
print(idata)


# 2 slice
population = idata[:, 1:]     # drop first col
print(population)


# 3 mean
popMean = np.mean(population, axis=0)   # col mean
print(popMean)


# 4 std
popStd = np.std(population, axis=0)     # col std
print(popStd)


# 5 broadcasting
A = np.tile(np.arange(0, 40, 10), (4, 1))  # repeat rows
print(A)


# 6 flatten
a = np.array([
    [[2, 4, 6], [1, 3, 5]],
    [[7, 9, 11], [8, 10, 12]]
])
print(a)
print(a.shape)

b = a.ravel()          # flatten
print(b)
print(b.shape)


# 7 reshape
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print(a.shape)
print(a)
