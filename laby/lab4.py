# lista = [i * 2 for i in range(31)]
# lista = str(lista)
# plik = open("plik.txt", 'a')
# plik.write(lista)
# plik.close

# plik = open("plik.txt", 'r')
# odczyt = plik.read()
# plik.close
# print(odczyt)

# with open("plik.txt", 'w') as plik:
#     plik.write("a\nm\ne\nn")
# with open("plik.txt", 'r') as plik:
#     odczyt = plik.read()
#     print(odczyt)

class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(self.nazwa_produktu)

    def ile_produktu(self):
        print(str(self.ilosc) + self.jednostka_miary)

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed


produkt = NaZakupy("mleko", 2, 'L', 4.5)
produkt.wyswietl_produkt()
produkt.ile_produktu()
print(produkt.ile_kosztuje())
