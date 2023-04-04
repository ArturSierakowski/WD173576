# def get_sum_of_digits(*num):
#     sum = 0
#     digits = list(num)
#     for x in digits:
#         sum += x
#     return sum
#
#
# print(get_sum_of_digits(1, 3, 3, 7))

# n = int(input("podaj n "))
# m = int(input("podaj m "))
# wynik = n
# while wynik < m:
#     print(wynik)
#     wynik += n

# for i in range(1, 51):
#     print(i, 100 - i)

# for liczba in range(10000):
#     suma = 0
#     dzielnik = 1
#     while dzielnik < liczba:
#         if liczba % dzielnik == 0:
#             suma += dzielnik
#         dzielnik += 1
#     if (liczba == suma):
#         print(liczba)

liczba = 12345
palindrom = 0
while liczba > 0:
    palindrom *= 10
    palindrom += liczba % 10
    liczba //= 10
print(palindrom)
