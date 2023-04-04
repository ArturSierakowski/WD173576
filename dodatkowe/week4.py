# A = [i for i in range(21) if i % 2 == 0]
# print(A)

# tekst = "Elo Elo Stara trze ser sobie tu na tarce Twój stary kręci się jak bęben w pralce"
# slowa = tekst.split()
# B = [len(slowo) for slowo in slowa]
# print(B)

# C = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
# print(C)

# slowo1 = "dmneawq3nM@N#RWFZ"
# slowo2 = " rfjmny32ys8mahsnAYuMn!y~m~u~("
# D = set(slowo1) | set(slowo2)
# print(D)

# zdanie = "cjn dcfjswj jsfdfb bdb ff"
# E = {}
# for slowo in zdanie.split():
#     E[slowo] = len(slowo)
# print(E)

import random
random.seed(123456)
randomlist = [random.randrange(1, 51) for i in range(51)]
# print(randomlist)

# ZADANIE 1
# suma = 0
# for i in randomlist:
#     suma += randomlist[i]
# print(suma)

# ZADANIE 2
# minimum = randomlist[0]
# for i in randomlist:
#     if randomlist[i] < minimum:
#         minimum = randomlist[i]
# print(minimum)
# print(min(randomlist))

# ZADANIE 3
# maksimum = randomlist[0]
# for i in randomlist:
#     if randomlist[i] > maksimum:
#         maksimum = randomlist[i]
# print(maksimum)
# print(max(randomlist))

# ZADANIE 4
lista = [1, 3, 2, 4, 5, -1]
# lista.sort()
# dl = len(lista)
# if dl % 2 == 0:
#     mediana = (lista[dl // 2] + lista[dl // 2 - 1]) / 2
# else:
#     mediana = lista[dl // 2]
# print(mediana)

# ZADANIE 5
sort = randomlist.copy()
# sort.sort()
# for i in range(len(sort)):
#     min = sort[i]
#     min_id = i
#     for j in range(i + 1, len(sort)):
#         if sort[j] < min:
#             min = sort[j]
#             min_id = j
#     tmp = sort[min_id]
#     sort[min_id] = sort[i]
#     sort[i] = tmp

# for i in range(len(sort)):
#     for j in range(i + 1, len(sort)):
#         if sort[j] < sort[i]:
#             sort[i], sort[j] = sort[j], sort[i]
#
# for i in range(20):
#     print(sort[i], end=' ')

# ZADANIE 6
# iloczyn = 1
# for i in range(len(lista)):
#     iloczyn *= lista[i]
# print(iloczyn)

# ZADANIE 7
# ilosc = 0
# for i in range(len(randomlist)):
#     if randomlist[i] // 10 > 0 and randomlist[i] // 10 < 10:
#         ilosc += 1
# print(ilosc)

# ZADANIE 8
czestosc = {}
for liczba in randomlist:
    if liczba not in czestosc:
        czestosc[liczba] = 1
    else:
        czestosc[liczba] += 1

najczestsza = None
naj_ilosc = 0
for liczba, ile in czestosc.items():
    if ile > naj_ilosc:
        najczestsza = liczba
        naj_ilosc = ile
print(najczestsza, naj_ilosc)
