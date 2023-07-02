import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# ZESTAW 2
# plt.subplot(1, 2, 1)
# y = np.arange(5)
# x1 = [54, 22, 83, 89, 80]
# kolory = ['midnightblue', 'darkturquoise', 'sandybrown', 'darkorange', 'mediumspringgreen']
# plt.barh(y, x1, color=kolory)
# plt.yticks(y, [5, 2, 6, 5, 4])
# plt.xlim(0, 100)
# plt.title("Tytuł2")
# for p in y:
#     plt.annotate(x1[p], xy=(x1[p] + 2, y[p]))
#
# plt.subplot(1, 2, 2)
# x2 = [-53, -83, -77, -14, -76]
# kolory = ['hotpink', 'mediumvioletred', 'plum', 'slategray', 'mediumblue']
# plt.barh(y, x2, color=kolory)
# plt.yticks(y, [1, 4, 6, 8, 8])
# plt.xlim(-100, 0)
# plt.title("Tytuł1")
# for p in y:
#     plt.annotate(x2[p], xy=(x2[p] - 10, y[p]))
# plt.tight_layout()
# plt.savefig('p2.jpg')
# plt.show()

# ZESTAW 3
# plt.subplot(2, 1, 1)
# etykiety = ['A', 'B', 'C', 'D', 'E']
# wartosci = [14, 24, 17, 24, 21]
# kolory = ['blueviolet', 'yellowgreen', 'mediumorchid', 'rosybrown', 'maroon']
# explode = [0.1, 0, 0, 0, 0]
# plt.pie(wartosci, labels=etykiety, colors=kolory, explode=explode, autopct='%1.f%%')
# plt.legend(loc='best', bbox_to_anchor=(0, -0.7))
# plt.title("Tytuł1")
#
# plt.subplot(2, 1, 2)
# wartosci = [74, 94, 83, 38, 76]
# kolory = ['orchid', 'blueviolet', 'chartreuse', 'darkgray', 'mediumslateblue']
# plt.pie(wartosci, labels=wartosci, colors=kolory, explode=explode)
# plt.title("Tytuł2")
# plt.savefig("p3.jpg")
# plt.show()

# ZESTAW 7
# etykiety = np.arange(14)
# banki = ['BOŚ', 'CitiHandlowy', 'BankPocztowy', 'Eurobank', 'CreditAgricole', 'SantanderCB', 'BankMillennium',
#          'BGŻBNPParibas', 'mBank', 'AliorBankiTMUB', 'INGBankŚląski', 'SantanderBP', 'BankPekao', 'PKOBPInteligo']
# wartosci = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 200]
#
# plt.barh(etykiety, wartosci, color='orange')
# plt.yticks(etykiety, banki)
# plt.xticks(np.arange(0, 200, 50))
# plt.grid()
# plt.title("Liczba klientów banków w IV kwartale 2018")
# plt.tight_layout()
# plt.savefig('p7.jpg')
# plt.show()

# ZESTAW 11
# fig, ax1 = plt.subplots()
# x = np.arange(3, 19, 0.1)
# ax1.plot(x, x - 4, label='x-4', color='brown')
# ax1.plot(x, -2 * x + 12, label='-2*x+12', color='cyan', linestyle='-.')
# ax1.set_xlim(2, 20)
# ax1.set_ylim(-12, 12)
# ax1.set_xlabel('oś pozioma', color='purple')
# ax1.set_ylabel('oś pionowa po lewej stronie')
# ax1.set_yticks(np.arange(-10, 15, 5))
# ax1.legend(loc='upper left')
#
# ax2 = ax1.twinx()
# ax2.plot(x, np.log(x), label='log nat. z x', color='k', linestyle=':')
# ax2.set_ylim(-4, 4)
# ax2.set_ylabel('oś pionowa po prawej stronie')
# ax2.legend(loc='center right')
# plt.title("Wykresy - kilka")
# plt.tight_layout()
# plt.savefig('p11.jpg')
# plt.show()
