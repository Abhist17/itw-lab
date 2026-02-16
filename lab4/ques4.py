# Basic Data Types in Python (NumPy)
import numpy as np

# 1
arr = np.arange(12)  # this will create an array of integer elements
print(type(arr))
print(arr.dtype)


# 2
# To create an array of float we have to mention explicitly
arrF = np.arange(8, dtype="float64")
print(arrF)
print(type(arrF))
print(arrF.dtype)


# 3
zarr = np.zeros((6, 6), dtype="int32")
print(type(zarr))
print(zarr.dtype)


# 4
xarr = np.array([5+12j, 7+15j])
print(type(xarr))
print(xarr.dtype)


# 5
barr = np.array([False, True, False])
print(type(barr))
print(barr.dtype)


# 6
sarr = np.array(["NumPy", "Python", "DataScience"])
print(sarr)
print(type(sarr))
print(sarr.dtype)
