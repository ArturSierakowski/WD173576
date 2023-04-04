# import math
# ZADANIE 1
# a = int(input("podaj a "))
# b = int(input("podaj b "))
# wynik = a*a + a*b + b*b
# wynik = str(wynik)
#
# try:
#     print(wynik)
# except ValueError:
#     if type(a) != int and type(b) != int:
#         print("wczytane liczby nie sa calkowite")
#
# plik = open("wynik.txt", 'w')
# plik.write(wynik)
# plik.close()

# ZADANIE 2
list1 = [1, 2, 3]
list2 = [4, 2, 1]


# def suma_elementow(list_a, list_b):
#     list_c = []
#     for i in range(len(list_a)):
#         list_c.append(list_a[i] + list_b[i])
#     return list_c
#
#
# list3 = suma_elementow(list1, list2)
# print(list3)

# ZADANIE 3
plik = open("tekst.txt", 'r', encoding="utf-8")
tekst = plik.read()
znaki = tekst[100:135]
print(znaki)

# ZADANIE 4
# lista = [3, 2, -3, 7, 4, 5]
# a = 2
# lista_a = [lista[i] for i in range(len(lista)) if lista[i] > a]
# print(lista_a)

# ZADANIE 5
# dzialanie = pow(pow(math.e, 3) + pow(math.cos(39), 2), (1/5)) + pow(2/7, 3) + math.pi
# print(round(dzialanie, 2))
# skrocone_dzialanie = (math.e**3 + math.cos(39)**2)**(1/5) + (2/7)**3 + math.pi
# print(skrocone_dzialanie)
