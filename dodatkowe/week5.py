import math

# ZADANIE 1
# def cg(n, a, q):
#     for i in range(1, n):
#         a *= q
#     return a
#
#
# print(cg(5, 2, 2))
# print(cg(10, 2, 1.01))


# ZADANIE 2
# def czy_sort(list):
#     for i in range(len(list) - 1):
#         if list[i] < list[i + 1]:
#             return False
#     return True
#
#
# lista1 = [5, 2, 3, 1, 2]
# lista2 = [3, 3, 3, 2, 2, 1]
# print(czy_sort(lista1))
# print(czy_sort(lista2))


# ZADANIE 3
# def suma_kwad(* liczby):
#     suma = 0
#     for i in liczby:
#         suma += i ** 2
#     return suma
#
#
# print(suma_kwad(1, 2, 3))
# print(suma_kwad(4, 5))


# ZADANIE 4
# def srednia_wieku(** kwargs):
#     suma = 0
#     for value in kwargs.values():
#         suma += value
#     return suma / len(kwargs)
#
#
# print(srednia_wieku(Adam=21, Artur=20, Joanna=49, Konrad=28))

# ZADANIE 5
# licznik = 0
#
#
# def funkcja():
#     global licznik
#     licznik += 1
#     print(f"funkcja wywolana {licznik} razy")
#
#
# funkcja()
# funkcja()

# ZADANIE 6
print(math.comb(5, 3))
print(math.fabs(-3.4))
print(math.fsum([4, 9, -2, 33, 11]))
print(math.gcd(60, 24))
print(math.floor(math.sqrt(5)))
print(math.exp(6))
print(math.log(5, 2))
print(math.log10(5))
print(math.log(6))
print(math.log(625, 5))
print(math.asin(1/2))
tau = 2 * math.pi
print(tau / 2)


# ZADANIE 7
def calculate_tax(income, /, *, tax_rate=0.1):
    return income * tax_rate


print(calculate_tax(1000))
