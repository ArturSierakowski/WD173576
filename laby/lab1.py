# a = "napis"
# print(a)
# print(type(a))
# b = "aaaa"
# print(a+b)
#
# b = 5
# print(a+str(b))
#
# c = 8
# d = 3
# print (c, d)
#
# e = c+d
# print(e)
#
# f = 2+3j
# print(f)
# print(type(f))
#
# print(c-d)
# print(c//d)
# print(c % d)
# print(c**d)
# print(2**(1/2))
# print(c+2)
#
# c += 2
# print(c)

# listy

listy = [2, 5, 6, 7, 6.5]
# print(listy)
#
# listy.append(4)
# print("wstawienie elementu na koniec", listy)
#
# listy.insert(4, 2)
# print("wstawienie elementu na indeks", listy)
#
# listy.remove(4)
# print("usuniecie elementu o wartosci", listy)
#
# listy.pop(2)
# print("usuniecie elementu z pozycji 2", listy)
#
# listy.sort()
# print("sortowanie listy", listy)
#
# listy.extend([1, 2, 3])
# print("dodanie sekwencji", listy)
#
# listy.reverse()
# print("odwrocenie listy", listy)

# dictionary

# slownik = {1: 'a', 2: 'b', 3: 'c'}
# print(slownik)
# print()

# wprowadzanie zmiennych

# napis = input('wprowadz liczbe: ')
# print(napis)
# print(type(napis))
# napis = int(napis)
# print(type(napis))

# instrukcje warunkowe

# a = input('podaj a: ')
# b = input('podaj b: ')
# a = int(a)
# b = int(b)
#
# if a > b:
#     print("a wieksze od b")
# elif a == b:
#     print("a jest rowne b")
# else:
#     print("a jest mniejsze od b")

# petle

# for i in range(5):
#     print(i)
# else:
#     print('koniec petli')
#
# for i in listy:
#     print(i)
#
# for i in range(len(listy)):
#     print(listy[i])

# i = 0
# while i < len(listy):
#     print(listy[i])
#     i += 1

liczby = [2, 5, 6, 2, 7, 3, 2, 4]
# a = input('podaj a: ')
# a = int(a)
# i = 0
# while i < len(liczby):
#     if liczby[i] - a == 0:
#         print(str(a) + ' - ' + str(liczby[i]) + ' = 0')
#     else:
#         print(i)
#     i += 1

for i in range(liczby.count(2)):
    liczby.remove(2)
print(liczby)

i = 0
while i < len(liczby):
    if liczby[i] == 2:
        liczby.pop(i)
    else:
        i += 1
print(liczby)
