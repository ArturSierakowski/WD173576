# import random

# A = [1-x for x in range(1, 11, 1)]
# print(A)
# B = [4**i for i in range(8)]
# print(B)
# C = [x for x in B if x % 2 == 0]
# print(C)

# lista1 = [random.randint(0, 5) for i in range(10)]
# lista2 = [i for i in lista1 if i % 2 == 0]
# print(lista1)
# print(lista2)

# produkty = {"masło": "kg", "mleko": "l", "ananas": "sztuki", "przyprawy": "g", "ogorki": "sztuki"}
# sztuki = [i for i in produkty if produkty[i] == "sztuki"]
# print(sztuki)

# def czy_prostokatny(a=5, b=12, c=13):
#     if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
#         return True
#     else:
#         return False
#
#
# print(czy_prostokatny())


# def pole_trapezu(a=3, b=4, h=2):
#     return (a + b) * h / 2
#
#
# print(pole_trapezu())


# def iloczyn(a=1, b=4, ile=10):
#     elementy = [a * (b ** i) for i in range(ile)]
#     wynik = 1
#     for i in elementy:
#         wynik *= i
#     return wynik
#
#
# print(iloczyn())

def iloczyn2():
    print("nic")


iloczyn2()

# zakupy = {"mleko": 4, "masło": 6, "chleb": 4, "ser": 8, "twarozek": 5}
#
#
# def koszt(lista):
#     print(len(lista))
#
#
# koszt(zakupy)
