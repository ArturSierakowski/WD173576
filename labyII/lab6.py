import numpy as np

# ZADANIE 1
# a = np.array([2, -1, 3])
# b = np.array([1, 4, -2])
#
# print(a * b)

# ZADANIE 2
# A = np.array([[2, -1, 3], [1, 7, 6], [9, 4, -2]])
# # print(A)
# for row in A:
#     print(np.min(row), end=' ')
# print("")
# for col in A.transpose():
#     print(np.min(col), end=' ')
# print("")
#
# B = np.array([[5, 8, 3, 1], [9, 2, 6, 5], [4, 7, 6, 3], [2, 8, 1, 9]])
# # print(B)
# for row in B:
#     print(np.min(row), end=' ')
# print("")
# for col in B.transpose():
#     print(np.min(col), end=' ')
# print("")

# ZADANIE 3
# c = np.dot(a, b)
# print(c)

# ZADANIE 4
# a = np.array([1, 2, 3], dtype='int32')
# b = np.array([1, 3, -2], dtype='float32')
# print(a*b)

# ZADANIE 5
# A = np.array([[1, 2], [4, 5], [7, 8]])
# a = np.sin(A)
# print(a)

# ZADANIE 6
# B = np.array([[1, -2], [-4, 5], [7, -8]])
# b = np.sin(B)
# print(b)

# ZADANIE 7
# print(a + b)

# # ZADANIE 8
# C = np.arange(2, 19, 2).reshape((3, 3))
# for row in C:
#     print(row)

# ZADANIE 9
# D = np.arange(9).reshape(3, 3)
# for el in D.flat:
#     print(el)

# ZADANIE 10
# E = np.arange(81).reshape(9, 9)
# print(E.ravel)
# print(E.reshape(3, 27))
# print(E.reshape(27, 3))
# print(E.reshape(81, 1))
# JEST NIEPARZYSTA

# ZADANIE 11
F = np.arange(12)
G = F.copy().reshape(4, 3)
H = F.copy().reshape(2, 6)

print(F.flatten(), G.flatten(), H.flatten())
