from builtins import classmethod
from datetime import *
import math


class Kolcsonzes:
    def __init__(self, sor: str):
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.az = adatok[1]
        self.ido1 = time(int(adatok[2]), int(adatok[3]))
        self.ido2 = time(int(adatok[4]), int(adatok[5]))

    def f_ido(self):
        return f'\t{self.ido1.hour:02}:{self.ido1.minute:02} - {self.ido2.hour:02}:{self.ido2.minute:02}'

    def f_adatok(self):
        return f'\t{self.ido1.hour:02}:{self.ido1.minute:02} - {self.ido2.hour:02}:{self.ido2.minute:02} : {self.nev}'

    # def percek(self, ido):
    #     return ido


    @classmethod
    def beolvas(cls, filename):
        lista = []
        with open(filename, 'r', encoding="UTF-8") as file:
            file.readline()
            for sor in file:
                k = cls(sor.strip())
                lista.append(k)
        return lista

    @classmethod
    def percek(cls, ido):
        return ido.hour * 60 + ido.minute


def main():
    kolcsonzesek = Kolcsonzes.beolvas('kolcsonzesek.txt')
    print('5. feladat: Napi kölcsönzések száma:', len(kolcsonzesek))

    nev = input('6. feladat: Kérek egy nevet: ')
    print(f'\t{nev} kölcsönzései:')
    talalt = False
    for k in kolcsonzesek:
        if k.nev == nev:
            print(k.f_ido())
            talalt = True
    if not talalt:
        print('\tNem volt ilyen nevű kölcsönző!')

    ip = input('7. feladat: Adjon meg egy időpontot óra:perc alakban: ').split(':')
    idopont = time(int(ip[0]), int(ip[1]))
    print('\tA vízen lévő járművek:')
    for k in kolcsonzesek:
        if idopont >= k.ido1 and idopont <= k.ido2:
            print(k.f_adatok())

    bevetel = 0
    for k in kolcsonzesek:
        felorak = math.ceil((Kolcsonzes.percek(k.ido2) - Kolcsonzes.percek(k.ido1)) / 30)
        bevetel += felorak * 2400
    print(f'8. feladat: A napi bevétel: {bevetel} Ft')

    with open('F.txt', 'w', encoding='UTF-8') as outfile:
        for k in kolcsonzesek:
            if k.az == "F":
                outfile.write(f'{k.f_adatok()}\n')

    print('10. feladat: Statisztika')
    stat = {}
    for k in kolcsonzesek:
        if not(k.az in stat):
            stat[k.az] = 1
        else:
            stat[k.az] += 1

    # for item in stat:
    #     print(f'\t{item} - {stat[item]}')

    stat_sort = sorted(stat.items())
    for t in stat_sort:
        print(f'\t{t[0]} - {t[1]}')


main()
