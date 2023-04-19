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
def srednia_wieku(** kwargs):
    suma = 0
    for value in kwargs.values():
        suma += value
    return suma / len(kwargs)


print(srednia_wieku(Adam=21, Artur=20, Joanna=49, Konrad=28))
