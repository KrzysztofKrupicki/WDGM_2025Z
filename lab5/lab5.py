import random

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import ImageChops
from PIL import ImageStat as Stat

im = Image.open('obraz.png')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
""" === === === Zadanie 1 === === === 
Pobierz statystyki obrazu im i je skomentuj
a. przedstaw histogram obrazu im na diagramie plt, przedstaw histogramy wszystkich jego kanałów na
diagramach plt.
b. Ile jest pikseli o wartości 155 na każdym z kanałów?
c. Napisz funkcję zlicz_piksele(obraz, kolor), która zlicza, ile jest pikseli w danym kolorze. Ile jest pikseli
o wartości [155,155,155] w obrazie im?
"""


def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.figure(figsize=(16, 16))
    plt.subplot(2, 2, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
    plt.title("histogram kanału R")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.subplot(2, 2, 2)
    plt.title("histogram kanału G")
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.5)
    plt.subplot(2, 2, 3)
    plt.title("histogram kanału B")
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.5)
    plt.subplot(2, 2, 4)
    plt.title("histogram")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)
    plt.savefig('histogramy.png')


rysuj_histogram_RGB(im)
"""
b. Ile jest pikseli o wartości 155 na każdym z kanałów?
"""
im_histogram = im.histogram()
print(f'Kanał R: {im_histogram[155]}')
print(f'Kanał G: {im_histogram[155 + 256]}')
print(f'Kanał B: {im_histogram[155 + 2 * 256]}')
print('\n')
"""
c. Napisz funkcję zlicz_piksele(obraz, kolor), która zlicza, ile jest pikseli w danym kolorze. Ile jest pikseli o wartości [155,155,155] w obrazie im?
"""


def zlicz_piksele(obraz, kolor):
    t = np.asarray(obraz)
    liczba_pikseli = np.sum(np.all(t == np.array(kolor), axis=-1))
    print(f'Łącznie pikseli o wartości {kolor}: {liczba_pikseli}')


zlicz_piksele(im, [155, 155, 155])


def statystyki(im):
    s = Stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


""" === === === Zadanie 2 === === === 
Zapisz obraz im w formacie jpg a potem wczytaj jako im_jpg.
    a. Porównaj statystyki obrazów im oraz im_jpg. Dla czego te obrazy się różnią?
    b. Zastosuj ImageChops.difference, aby otrzymać różnicę tych obrazów. Pobierz statystyki różnicy i je
    skomentuj
    c. Jak zmienią się statystyki, gdy jeszcze dwa razy zapiszesz obraz im_jpg w formacie jpg?
"""
im_jpg = Image.open('obraz.jpg')
im_jpg3 = Image.open('obraz3.jpg')
print(f'===== Statystyki obrazu PNG =====')
statystyki(im)
print(f'===== Statystyki obrazu JPG =====')
statystyki(im_jpg)
print(f'===== Statystyki obrazu różnic =====')
diff = ImageChops.difference(im, im_jpg)
statystyki(diff)
"""
Odpowiedź:
Obrazy róźnią się ponieważ zapisując obraz w formacie JPG następuje kompresja stratna, tracimy część danych obrazu.
Ekstrema nie zmieniły się (mamy pełny zakres barw). 
Średnia różni się minimalnie, największa różnica w kanale niebieskim, co oznacza że utraciliśmy najwięcej niebieskiej barwy.
Mediana przesuneła się w kanale niebieskim o 3 wartości, wprowadziła lekką zmianę barwy.
Mniejsze odchylenie standardowe w JPG oznacza rozmycie szczegółów.
Minimalny spadek RMS, czyli mamy drobną utratę szczegółów i kontrastu.
"""
"""
c. Jak zmienią się statystyki, gdy jeszcze dwa razy zapiszesz obraz im_jpg w formacie jpg?
"""
print(f'===== Statystyki obrazu 3xJPG =====')
statystyki(im_jpg3)
print(f'===== Statystyki różnic PNG vs 3xJPG =====')
diff2 = ImageChops.difference(im, im_jpg3)
statystyki(diff2)
diff2.show()
"""
Po zapisaniu jeszcze dwa razy jako JPG:
Średnia rośnie, kolory stają się jaśniejsze - tracimy kontrast.
Mniejsze ochylenie standardowe, większe rozmycie szczegółów.
Niewielka zmiana mediany.
Dalszy spadek RMS to spadek kontrastu i energii obrazu.

Każde kolejne zapisanie pliku JPG powoduje kumulację strat.
Kompresja działa na już skompresowanych danych, więc pojawia się coraz większe rozmycie, kolory się lekko zmieniają, kontrast i ostrość maleją, statystyki (stddev, RMS) spadają systematycznie.
"""
""" === === === Zadanie 3 === === === 
Wykonaj następujące polecenia dla obrazu im
    a. Wczytaj tablicę obrazu i pobierz kanały t_r, t_g, t_b obrazu z tablicy obrazu, zapisz jako obrazy im_r, im_g, im_b
    b. Utwórz obraz im1 przez scalenie metodą merge obrazów im_r, im_g, im_b i zastosuj ImageChops.difference(im, im1) do porównania otrzymanego obrazu z obrazem wejściowym.
    c. Umieść na jednej figurze plt (fig1.png) obrazy im, im1 i wynik porównania
    d. Czy są jakieś różnice?
"""
t = np.asarray(im)
t_r = t[:, :, 0]
t_g = t[:, :, 1]
t_b = t[:, :, 2]
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)
im1 = Image.merge("RGB", (im_r, im_g, im_b))
diff = ImageChops.difference(im, im1)
"""
c. Umieść na jednej figurze plt (fig1.png) obrazy im, im1 i wynik porównania
"""
plt.figure(figsize=(16, 12))
plt.subplot(2, 2, 1)
plt.title("Oryginalny obraz - im")
plt.axis('off')
plt.imshow(im)
plt.subplot(2, 2, 2)
plt.title("Po scaleniu - im1")
plt.axis('off')
plt.imshow(im1)
plt.subplot(2, 2, 3)
plt.title("Różnica")
plt.axis('off')
plt.imshow(diff)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
plt.show()
"""
d. Czy są jakieś różnice?
"""
print(f'===== Statystyki różnic =====')
statystyki(diff)
"""
Odpowiedź:
Nie widać różnic w obrazach, wszystkie statystyki w obrazie różnic to 0, czyli otrzymany obraz w wyniku złączenia trzech kanałów jest taki sam jak oryginał.
"""
""" === === === Zadanie 4 === === === 
Napisz funkcję mieszaj_kanaly(obraz), która w sposób losowy miesza kanały r, g, b pobrane metodą split z
danego obrazu oraz ich negatywy nr,ng,nb. Dopuszczalne jest losowanie z powtórzeniami tzn. może być b, r,
g ale też b, b, g .
    a. Zastosuj tę funkcje do obrazu im. Otrzymany obraz nazwij mix i zapisz w formacie png.
    b. Napisz funkcję rozpoznaj_mix(obraz, mix), która dla danych obrazów w trybie RGB obraz i mix rozpoznaje w jaki sposób mix powstał z obrazu (zmiana kolejności kanałów). 
"""


def mieszaj_kanaly(obraz):
    r, g, b = obraz.split()
    nr = Image.fromarray(255 - np.array(r))
    ng = Image.fromarray(255 - np.array(g))
    nb = Image.fromarray(255 - np.array(b))
    kanaly = [r, g, b, nr, ng, nb]
    nazwy_kanalow = ["R", "G", "B", "negatyw R", "negatyw G", "negatyw B"]
    wybrane = random.choices(kanaly, k=3)
    mix = Image.merge("RGB", wybrane)
    wybrane_nazwy = [nazwy_kanalow[kanaly.index(k)] for k in wybrane]
    # print("Wybrane kanały:", wybrane_nazwy)
    return mix


mix = mieszaj_kanaly(im)
mix.show()
mix.save('mix.png')
"""
b. Napisz funkcję rozpoznaj_mix(obraz, mix), która dla danych obrazów w trybie RGB obraz i mix
rozpoznaje w jaki sposób mix powstał z obrazu (zmiana kolejności kanałów). 
"""


def rozpoznaj_mix(obraz, mix):
    r, g, b = obraz.split()
    nr = Image.fromarray(255 - np.array(r, dtype=np.uint8))
    ng = Image.fromarray(255 - np.array(g, dtype=np.uint8))
    nb = Image.fromarray(255 - np.array(b, dtype=np.uint8))

    oryginalne_kanaly = [r, g, b, nr, ng, nb]
    nazwy_kanalow = ["R", "G", "B", "negatyw R", "negatyw G", "negatyw B"]
    wynik = []

    for mix_kanal in mix.split():
        for nazwa, k in zip(nazwy_kanalow, oryginalne_kanaly):
            if np.all(np.array(mix_kanal) == np.array(k)):
                wynik.append(nazwa)
                break
    print('Rozpoznano:')
    print(f'R -> {wynik[0]}')
    print(f'G -> {wynik[1]}')
    print(f'B -> {wynik[2]}')


rozpoznaj_mix(im, mix)
""" === === === Zadanie 5 === === === 
Dlaczego polecenie r, g, b = im.split() nie działa, gdy im = Image.open('beksinski1.png')?
"""
im = Image.open('beksinski.png')
im1 = Image.open('beksinski1.png')
print('===== beksinski.png =====')
print(im.mode)
print('===== beksinski1.png =====')
print(im1.mode)
# r, g, b = im1.split()
"""
Odpowiedź:
Polecenie nie działa, ponieważ mamy 4 kanały (obraz RGBA), a podajemy tylko 3 zmienne, kanał 4 jest od alpha, czyli przeźroczystość.
"""
