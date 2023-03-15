import math

# print(math.exp(10))
# print(math.log(5 + pow(math.sin(8), 2))**(1/6))
# print(math.floor(3.55))
# print(math.ceil(4.80))

# imie = "ARTUR"
# nazwisko = "SIERAKOWSKI"
# imie = imie.capitalize()
# nazwisko = nazwisko.capitalize()
# print(imie, nazwisko)

# napis = "Na na, la la la la la na na na na na"
# print(napis.count("la"))

piwo = "tyskie"
# print(piwo[1], piwo[-1])

zdanie = "wypilem " + piwo + " na hita"
# zdanie = zdanie.split()
# print(zdanie)

# x = str(21)
# y = float(21)
# z = hex(21)
# print(x, y, z)

# sporty = ["plywanie", "rower", "narty"]
# sporty.reverse()
# sporty.append("kosz")
# sporty.append("siata")
# print(sporty)

# slownik_skrotow = {"np": "na przyklad", "tzw": "tak zwany"}
# print(slownik_skrotow)

# slownik_gier = {"CoD": "Call of Duty", "CS": "Counter Strike", "WoW": "World of Warcraft", "LoL": "Liga Legend"}
# print(len(slownik_gier), slownik_gier)

# zdanie = input("wprowadz zdanie: ")
# print(zdanie.count('a'))

# a = input("wprowadz a: ")
# b = input("wprowadz b: ")
# c = input("wprowadz c: ")
# a = int(a)
# b = int(b)
# c = int(c)
#
# if a >= b and a >= c:
#     print(a, "jest najwieksza")
# elif b >= a and b >= c:
#     print(b, "jest najwieksza")
# elif c >= a and c >= b:
#     print(c, "jest najwieksza")

lista = [5, 3.5, 2, 4, 1.0, 1.2]
for i in range(len(lista)):
    print(lista[i] ** 2)

i = 0
liczby = []
while i < 10:
    n = input("wprowadz liczbe: ")
    n = int(n)
    if n % 2 == 0:
        liczby.append(n)
    i += 1
print(liczby)
