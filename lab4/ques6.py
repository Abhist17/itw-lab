import numpy as np

# 1
arrA = np.arange(15)

arrB = arrA[::4]  # arrB also points to arrA by sharing memory
print("arrA:", arrA)
print("arrB:", arrB)


# 2
arrA[8] = 444

print("\narrA:", arrA)  # Both arrA and arrB share the same memory
print("arrB:", arrB)


# 3
arrA = np.arange(15)

arrB = arrA[::4].copy()
print("arrA:", arrA)
print("arrB:", arrB)

print("Address of arrA:", id(arrA))
print("Address of arrB:", id(arrB))
print("\narrA & arrB share memory?", np.shares_memory(arrA, arrB))

arrB[2] = 888

print("\narrA:", arrA)  # arrA and arrB do NOT share memory
print("arrB:", arrB)


# 4
arr = np.arange(8)
print(arr)

mask = (arr % 2 == 0)
print(mask)

arrB = arr[mask]  # Boolean indexing creates a copy
print("arr:", arr)
print("arrB:", arrB)


# 5
arr[mask] = -8  # all places in arr where condition is True are replaced
print(arr)
