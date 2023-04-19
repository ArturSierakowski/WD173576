import math

# ZADANIE 1
dzialanie = (math.log(20) + math.cos(45) + math.e)**(1/3)
print(round(dzialanie, 2))

# ZADANIE 2
lista1 = [1, -2, 3.5, 3]
lista2 = [liczba for liczba in lista1 if liczba != min(lista1)]
print(lista1)
print(lista2)

# ZADANIE 3
# zakupy = {"mleko": 4.8, "chleb": 5.9, "czipsy": 7}
#
#
# def foo(slownik):
#     lista = []
#     for key in slownik.keys():
#         if type(slownik[key]) == float:
#             lista.append((key, slownik[key]))
#     return lista
#
#
# print(foo(zakupy))

liczby = {5: 4.8, 5.9: 6.1, 6.7: 7}

def foo2(slownik):
    lista = []
    for key, value in slownik.items():
        if type(key) == float and type(value) == float:
            lista.append((key, value))
    return lista


print(foo2(liczby))

# ZADANIE 4
plik = open("tekst.txt", 'r', encoding="utf-8")
odczyt = plik.read()
plik.close()
znaki = odczyt[16:57]
print(znaki)

ilosc_c = odczyt.count('c')
print(ilosc_c)

# ZADANIE 5
try:
    a = int(input("wprowadz a "))
    n = int(input("wprowadz n "))
    q = int(input("wprowadz q "))
    if n <= 0:
        raise ValueError
    wynik = a
    for i in range(1, n):
        wynik *= q

    file = open("wynik.txt", 'w')
    zapis = file.write(str(wynik))
    file.close()
except ValueError:
    print("wczytana liczba nie jest całkowita lub n nie jest naturalne")
