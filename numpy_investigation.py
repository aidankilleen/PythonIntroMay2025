# numpy_investigation.py

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])


print (a + b)
print (a * b)

a = np.array([[10, 20, 30, 35], [40, 50, 60, 65], [70, 80, 90, 95]])

print (a)

print (a[1, 2])

print (a[:, 1])

print (a[0:2, 1:])


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


print(a.reshape((2, 6)))
print(a.reshape((3, 4)))
print(a.reshape((4, 3)))
print(a.reshape((2, 6)))
print(a.reshape((12, 1)))


print (a.sum())
print (a.max())
print (a.mean())











