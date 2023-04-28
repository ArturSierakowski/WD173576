import numpy as np
import random

# ZADANIE 1
# A = np.arange(4, 4*21, 4)
# print(A)

# ZADANIE 2
# B = [1.0, 2.2, 3.1, -1.7]
# kopia = np.array(B, dtype='int32')
# print(kopia)


# ZADANIE 3
# def macierz_poteg(n):
#     potegi = np.power(2, np.arange(n * n))
#     tab = potegi.reshape(n, n)
#     return tab
#
#
# print(macierz_poteg(3))

# ROZWIAZANIE PROWADZACEGO
# def tablica(n):
#     a = np.zeros((n*n), dtype='int32')
#     for i in range(0, len(a)):
#         a[i] = 2**i
#     tab = a.reshape((n, n))
#     return tab
#
#
# print(tablica(5))


# ZADANIE 4
# def generuj(podstawa, wykladnik):
#     potegi = np.logspace(1, wykladnik, wykladnik, base=podstawa, dtype=int)
#     return potegi
#
#
# print(generuj(3, 6))


# ZADANIE 5
# def diagonal(n):
#     wektor = np.arange(1, n+1)[::-1]
#     macierz = np.diag(wektor, 2)
#     return macierz
#
#
# print(diagonal(3))

# ZADANIE 6
# wyrazy = ["python", "analiza", "danych"]
# litery = "abcdefghijklmnoprstuwyz"
# macierz = np.random.choice((list(litery)), (8, 8))
# macierz[2, 7:1:-1] = list(wyrazy[0])
# macierz[1:8, 2] = list(wyrazy[1])
# macierz[np.diag_indices(6)] = list(wyrazy[2])
# print(macierz)


# ZADANIE 7
def macierz(n):
    mac = np.full((n, n), 2)
    for i in range(1, n):
        mac += np.diag([2 * i for _ in range(n - i)], k=i)
        mac += np.diag([2 * i for _ in range(n - i)], k=-i)
    return mac


print(macierz(3))


# ZADANIE 8
# def podziel(tab, kierunek):
#     print(tab)
#     if kierunek == 'poziomo':
#         if tab.shape[0] % 2 != 0:
#             return
#         p1 = tab[0:int(tab.shape[0]/2), :]
#         p2 = tab[int(tab.shape[0]/2):, :]
#         print(p1)
#         print(p2)
#     elif kierunek == 'pionowo':
#         if tab.shape[1] % 2 != 0:
#             return
#         p1 = tab[:, 0:int(tab.shape[1]/2)]
#         p2 = tab[:, int(tab.shape[1]/2):]
#         print(p1)
#         print(p2)
#
#
# podziel(np.arange(16).reshape((4, 4)), kierunek='pionowo')


# ZADANIE 9
# def n_ty_wyraz(a1, n, r):
#     return a1 + n * r
#
#
# macierz = np.ones(25, dtype='int')
# for i in range(len(macierz)):
#     element = n_ty_wyraz(3, i, 3)
#     macierz[i] = element
#
# macierz = macierz.reshape((5, 5))
# print(macierz)
