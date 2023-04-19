import numpy as np

# SUMA MACIERZY
# a = np.array([10, 20, 30, 40])
# b = np.arange(4)
# print(a)
# print(b)
#
# c = a + b
# print(c)

# SUMA ELEMENTOW (axis=0 - KOLUMNY, axis=1 - WIERSZE)
# d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(d.sum())
# print(d.sum(axis=0))
# print(d.sum(axis=1))
# print(d.cumsum(axis=0))

# MNOZENIE MACIERZY
# a = np.array([[2, 1, 3], [-1, 2, 4]])
# b = np.array([[1, 3], [2, -2], [-1, 4]])
#
# c = np.dot(a, b)
# print(c)
#
# d = a.dot(b)
# print(d)

# TO CHYBA ZAMIENIA MACIERZ NA WEKTOR KOLUMNOWY
# a = np.arange(6).reshape((3, 2))
# print(a)
#
# # for b in a:
# #     print(b)
# print("")
# for c in range(0, a.shape[0], 1):
#     for d in range(0, a.shape[1], 1):
#         print(a[c][d])
#
# # for c in a.flat:
# #     print(c)

# ZMIENIANIE WYMIAROW MACIERZY, ZAMIENIANIE MACIERZY NA WEKTOR LINIOWY, TRANSPOZYCJA
# a = np.arange(6)
# print("a", a)
# print("wymiary", a.shape)
#
# b = a.reshape((2, 3))
# print("b", b)
#
# c = a.reshape((3, 2))
# print("c", c)
#
# d = a.reshape((6, 1))
# print("d", d)
# print("wymiary d", d.shape)
#
# e = c.ravel()
# print("splaszczanie?", e)
#
# print(c)
# f = c.T
# print("transpozycja c", f)
# print("wymiary c", f.shape)

# a = np.array([0, 1, 2])
# b = np.array([0, 1, 2])
#
# # MNOZENIE MACIERZY (PYTHON ZAMIENIA DOMYSLNIE WYMIARY MACIERZY b)
# c = np.dot(a, b)
# print(c)
#
# # MNOZENIE ELEMENTOW
# d = a * b
# print(d)
