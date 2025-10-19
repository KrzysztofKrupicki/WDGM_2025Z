from PIL import Image  # Python Imaging Library
import numpy as np

obrazek = Image.open('bs.bmp')


# Zadanie 1
def rysuj_ramke_w_obrazie(obraz, grub):
    tablica_obrazu = np.asarray(obraz, dtype='uint8')
    h, w = tablica_obrazu.shape
    tablica_obrazu[0:h, 0:grub] = 0  # lewy
    tablica_obrazu[0:h, w - grub:w] = 0  # prawy
    tablica_obrazu[0:grub, 0:w] = 0  # gorny
    tablica_obrazu[h - grub:h, 0:w] = 0  # dolny
    wynik = tablica_obrazu.astype(bool)
    return Image.fromarray(wynik)


rysuj_ramke_w_obrazie(obrazek, 12)


# Zadanie 2
def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)  # białe tło
    k = 0
    ile = int(min(w, h) / (2 * grub))
    for i in range(ile):
        lewo = i * grub
        prawo = w - i * grub
        gora = i * grub
        dol = h - i * grub

        tab[gora:gora + grub, lewo:prawo] = k % 2  # gora
        tab[dol - grub:dol, lewo:prawo] = k % 2  # dol
        tab[gora:dol, lewo:lewo + grub] = k % 2  # lewo
        tab[gora:dol, prawo - grub:prawo] = k % 2  # prawo
        k += 1

    tab_bool = tab.astype(bool)
    return Image.fromarray(tab_bool)


rysuj_ramki(120, 240, 8)


def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    k = 0
    ile = int(w / 2 * grub)
    for i in range(ile):
        lewo = i * grub
        tab[0:h, lewo:lewo + grub] = k % 2
        k += 1
    tab_bool = tab.astype(bool)
    return Image.fromarray(tab_bool)


rysuj_pasy_pionowe(240, 120, 8)


def rysuj_wlasne(w, h, grub, iteracje):
    """
    Rysuje zbiór Cantora.
    w, h        - wymiary obrazu
    grub        - grubość odcinków (piksele)
    iteracje    - liczba poziomów (iteracji)
    """
    tab = np.ones((h, w), dtype=np.uint8)
    segmenty = [(0, w, 0, iteracje)]

    while segmenty:
        lewo, prawo, y, poziom = segmenty.pop(0)

        if poziom == 0 or y >= h:
            continue

        tab[y:y + grub, lewo:prawo] = 0
        trzeci = (prawo - lewo) // 3
        nowy_y = y + 2 * grub
        if poziom > 1:
            segmenty.append((lewo, lewo + trzeci, nowy_y, poziom - 1))
            segmenty.append((prawo - trzeci, prawo, nowy_y, poziom - 1))

    tab_bool = tab.astype(bool)
    return Image.fromarray(tab_bool)


rysuj_wlasne(600, 120, 3, 8)


# Zadanie 3
def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_bazowy = np.asarray(obraz_bazowy).astype(np.uint8)
    tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)

    h_b, w_b = tab_bazowy.shape
    h_w, w_w = tab_wstawiany.shape

    # Wyznaczanie obszaru wstawienia (przycinamy, jeśli wychodzi poza granice)
    n_k = min(h_b, n + h_w)
    m_k = min(w_b, m + w_w)
    n_p = max(0, n)
    m_p = max(0, m)

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_bazowy[i, j] = tab_wstawiany[i - n, j - m]
    tab_bool = tab_bazowy.astype(bool)
    return Image.fromarray(tab_bool)


obrazek1 = Image.open('bs.bmp')
obrazek2 = Image.open('inicjaly.bmp')
wstaw_obraz_w_obraz(obrazek1, obrazek2, 35, 26)
