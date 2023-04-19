# A = [i for i in range(21) if i % 2 == 0]
# print(A)

# tekst = "Jade pociagiem do domu"
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
lista1 = [1, 3, 2, 4, 5, -1]
# lista1.sort()
# dl = len(lista1)
# if dl % 2 == 0:
#     mediana = (lista1[dl // 2] + lista1[dl // 2 - 1]) / 2
# else:
#     mediana = lista1[dl // 2]
# print(mediana)

# ZADANIE 5
sorted = randomlist.copy()

# PIERWSZY SPOSOB
# sorted.sort()
# print(sorted)

# DRUGI SPOSOB
# for i in range(len(sorted)):
#     min = sorted[i]
#     min_id = i
#     for j in range(i + 1, len(sorted)):
#         if sorted[j] < min:
#             min = sorted[j]
#             min_id = j
#     tmp = sorted[min_id]
#     sorted[min_id] = sorted[i]
#     sorted[i] = tmp

# TRZECI SPOSOB
# for i in range(len(sorted)):
#     for j in range(i + 1, len(sorted)):
#         if sorted[j] < sorted[i]:
#             sorted[i], sorted[j] = sorted[j], sorted[i]

# for i in range(20):
#     print(sorted[i], end=' ')

# ZADANIE 6
# iloczyn = 1
# for i in range(len(lista1)):
#     iloczyn *= lista1[i]
# print(iloczyn)

# ZADANIE 7
# ilosc = 0
# for i in range(len(randomlist)):
#     if 10 > randomlist[i] // 10 > 0:
#         ilosc += 1
# print(ilosc)
def czestosc(lista):
    ile_razy = {}
    for liczba in lista:
        if liczba not in ile_razy:
            ile_razy[liczba] = 1
        else:
            ile_razy[liczba] += 1
    return ile_razy


# ZADANIE 8
# najczestsza = None
# naj_ilosc = 0
# for liczba, ile in czestosc(randomlist).items():
#     if ile > naj_ilosc:
#         najczestsza = liczba
#         naj_ilosc = ile
# print(najczestsza, naj_ilosc)

# ZADANIE 9
# ile_razy = czestosc(randomlist)
# lista_raz = [i for i in ile_razy if ile_razy[i] == 1]
# print(lista_raz)

# ZADANIE 10
# ile_razy = czestosc(randomlist)
# lista_trzy = [i for i in ile_razy if ile_razy[i] == 3]
# print(lista_trzy)

# ZADANIE 11
# ile_wiekszych = 0
# for i in randomlist:
#     if randomlist[i] > 27:
#         ile_wiekszych += 1
# print(ile_wiekszych)

# ZADANIE 12
# print(czestosc(randomlist))

# ZADANIE 13
# a = 5
# b = 20
# ilosc = 0
# for i in randomlist:
#     if a <= randomlist[i] <= b:
#         ilosc += 1
# print(ilosc)

# ZADANIE 14
# parzyste = 0
# for i in randomlist:
#     if randomlist[i] % 2 == 0:
#         parzyste += 1
# print(parzyste)

# ZADANIE 14
# nieparzyste = 0
# for i in randomlist:
#     if randomlist[i] % 2 != 0:
#         nieparzyste += 1
# print(nieparzyste)
