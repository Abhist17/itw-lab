import numpy as np

# 1 logical ops
a = np.array([1, 0, 1, 0], dtype=bool)
b = np.array([0, 1, 1, 0], dtype=bool)

OR  = np.logical_or(a, b)    # OR
AND = np.logical_and(a, b)   # AND
XOR = np.logical_xor(a, b)   # XOR
NOT = np.logical_not(a)      # NOT

print("a :", a)
print("b :", b)
print()

print("OR :", OR)
print("AND:", AND)
print("XOR:", XOR)
print("!a :", NOT)


# 2 all()
check = np.all([True, 1, -5])   # all true?
print(check)

check = np.all([1, 0, 3])       # zero fails
print(check)

check = np.all([])              # empty
print(check)

print("@@@@")


# 3 any()
check = np.any([0, False, 5])   # any true?
print(check)

check = np.any([0, 0, 0])       # none true
print(check)

check = np.any([])              # empty
print(check)


# 4 array check
a = np.zeros((2, 2))
a[1][1] = 7
print(a)
print(np.all(a != 0))            # all nonzero?


# 5 chained compare
a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 4, 5])
c = np.array([3, 3, 5, 6])
print(((a <= b) & (b <= c)).all())


# 6 trig
a = np.arange(6)
print(a)
print(np.cos(a))                # cos


# 7 broadcasting
a = np.arange(3)
print(a.shape)
print(a + np.array([2]))        # broadcast
