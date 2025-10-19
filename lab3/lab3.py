from PIL import Image
import numpy as np


def rysuj_ramki_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8) * 255
    ile = int(min(w, h) / (2 * grub)) + 1
    szary = 0
    for i in range(ile):
        if i % 2 == 1:
            continue
        lewo = i * grub
        prawo = w - i * grub
        gora = i * grub
        dol = h - i * grub
        szary += zmiana_koloru
        tab[gora:gora + grub, lewo:prawo] = szary % 256  # gora
        tab[dol - grub:dol, lewo:prawo] = szary % 256  # dol
        tab[gora:dol, lewo:lewo + grub] = szary % 256  # lewo
        tab[gora:dol, prawo - grub:prawo] = szary % 256  # prawo
    return Image.fromarray(tab)


rysuj_ramki_szare(240, 120, 7, 32)


def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8) * 255
    ile = int(w / grub) + 1
    szary = 0
    for i in range(ile):
        lewo = i * grub
        if i % 2 == 1:
            continue
        tab[0:h, lewo:lewo + grub] = szary % 256
        szary += zmiana_koloru
    return Image.fromarray(tab)


rysuj_pasy_pionowe_szare(240, 120, 7, 10)


def negatyw(obraz):
    tablica_obrazu = np.asarray(obraz)
    tablica_negatyw = np.copy(tablica_obrazu)
    match obraz.mode:
        case '1':
            tablica_negatyw = ~tablica_obrazu
        case 'L':
            tablica_negatyw = 255 - tablica_obrazu
        case 'RGB':
            tablica_negatyw = 255 - tablica_obrazu
        case _:
            return None
    return Image.fromarray(tablica_negatyw)


gwiazdka = Image.open('gwiazdka.bmp')
gwiazdka_negatyw = negatyw(gwiazdka)


def rysuj_ramke_kolor(w, h, grub, kolor_ramki, kolor_tla):  # kolor_ramki, kolor podajemy w postaci [r, g, b]
    t = (h, w, 3)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy
    tab[:] = kolor_ramki  # wypełnienie tablicy kolorem kolor_ramki
    tab[grub:h - grub, grub:w - grub, 0] = kolor_tla[0]  # wartości kanału R
    tab[grub:h - grub, grub:w - grub, 1] = kolor_tla[1]  # wartości kanału G
    tab[grub:h - grub, grub:w - grub, 2] = kolor_tla[2]  # wartości kanału B
    # tab[grub:h - grub, grub:w - grub] = kolor_tla # wersja równoważna
    return Image.fromarray(tab)


# ramki_kolorowe_2b = rysuj_ramke_kolor(200, [20, 120, 220], len('Krzysztof'), len('Krupicki'), len('Krzysztof') * (-1))
# negatyw_2b = negatyw(ramki_kolorowe_2b)


def rysuj_po_skosie_szare(h, w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w)  # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a * i + b * j) % 256
    return Image.fromarray(tab)


po_skosie_szare_2c = rysuj_po_skosie_szare(100, 300, len('Krzysztof'), len('Krupicki'))
negatyw_2c = negatyw(po_skosie_szare_2c)


def rysuj_pasy_poziome_3kolory(w, h, grub):  # funkcja rysuje pasy poziome na przemian czerwony, zielony, niebieski
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if k % 3 == 0:
                    tab[i, j] = [255, 0, 0]
                elif k % 3 == 1:
                    tab[i, j] = [0, 255, 0]
                else:
                    tab[i, j] = [0, 0, 255]
    return Image.fromarray(tab)


obraz1 = rysuj_pasy_poziome_3kolory(200, 100, 10)


def koloruj_w_paski(obraz, grub, kolory=None):
    if kolory is None:
        kolory = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    tab = np.asarray(obraz).astype(np.uint8)
    h, w = tab.shape
    tab_nowego_obrazu = np.ones((h, w, 3), dtype=np.uint8) * 255

    ile = int(h / grub) + 1
    for i in range(ile):
        kolor = kolory[i % len(kolory)]
        for g in range(grub):
            wiersze = i * grub + g
            if wiersze >= h:
                break
            maska = (tab[wiersze, :] == 0)
            for c in range(3):
                tab_nowego_obrazu[wiersze, maska, c] = kolor[c]

    return Image.fromarray(tab_nowego_obrazu)


koloruj_w_paski(gwiazdka, 5)


def koloruj_w_paski_tlo(obraz, grub, kolory=None, kolor_tla=None):
    if kolory is None:
        kolory = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    if kolor_tla is None:
        kolor_tla = (134, 52, 169)
    tab = np.asarray(obraz).astype(np.uint8)
    h, w = tab.shape
    tab_nowego_obrazu = np.ones((h, w, 3), dtype=np.uint8) * np.array(kolor_tla, dtype=np.uint8)

    ile = int(h / grub) + 1
    for i in range(ile):
        kolor = kolory[i % len(kolory)]
        for g in range(grub):
            wiersze = i * grub + g
            if wiersze >= h:
                break
            maska = (tab[wiersze, :] == 0)
            for c in range(3):
                tab_nowego_obrazu[wiersze, maska, c] = kolor[c]

    return Image.fromarray(tab_nowego_obrazu)


koloruj_w_paski_tlo(gwiazdka, 5)

inicjaly = Image.open('inicjaly.bmp')
inicjaly_kolor_w_paski = koloruj_w_paski(gwiazdka, 5,
                                         kolory=[(123, 117, 84), (161, 22, 146), (255, 79, 121), (23, 24, 59),
                                                 (255, 180, 154)])
inicjaly_kolor_w_paski.save('inicjaly.jpg', 'JPEG')
inicjaly_kolor_w_paski.save('inicjaly.png', 'PNG')

# inicjaly = Image.open('../lab1/inicjaly.bmp')
# kolor_w_paski = koloruj_w_paski(inicjaly, 15)

"""
Zadanie 4

Przy 328 i -24 wyskakuje komuikat, że wartość jest poza zakresem. Typ uint8 oznacza liczbe bez znaku (dodatnią), całkowitą 8 bitową, więc jej zakres to 0-255.
"""
