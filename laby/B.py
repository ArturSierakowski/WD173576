import math

# ZADANIE 1
plik = open("tekst.txt", 'r', encoding="utf-8")
odczyt = plik.read()
znaki = odczyt[71:111]
print(znaki)
ilosc = odczyt.count('A')
if ilosc != 0:
    print("liter 'A' jest ", ilosc)
else:
    print("w tekscie nie ma litery 'A'")

# ZADANIE 2
lista1 = [1, 1.0, 2.0, 3.5, -2]
lista2 = [i for i in lista1 if type(i) == float]
print(lista2)


# ZADANIE 3
def foo(lista):
    suma = lista[0] + sum(lista)
    lista.append(suma)
    return lista


print(foo(lista1))

# ZADANIE 4
wynik = math.sin(56)**2 + (4**2 / 25 + math.log(85, 3))**(1/4)
print(round(wynik, 2))

# ZADANIE 5
try:
    n = int(input("wprowadz n"))
    wynik = 0
    for i in range(1, n + 1):
        wynik += i

    plik = open("zadanie5.txt", 'w')
    plik.write(str(wynik))
    plik.close()
except ValueError:
    print("wczytana liczba nie jest calkowita")
