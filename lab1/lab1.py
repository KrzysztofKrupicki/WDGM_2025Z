from PIL import Image
import numpy as np


print('\n=== Zadanie 2 ===')
obrazek = Image.open('inicjaly.bmp')
print("=== Informacje o obrazie ===")
print(f'Tryb: {obrazek.mode}')
print(f'Format: {obrazek.format}')
print(f'Rozmiar: {obrazek.size}')

# najpierw szerokosc, potem wysokosc
# 0 - False = Czarny
# 1 - True = Bialy


print('\n=== Zadanie 3 ===')
tablica_obrazka = np.asarray(obrazek)
tablica_obrazka_bin = tablica_obrazka.astype(np.int_)
print(tablica_obrazka_bin)
obraz_z_tablicy = Image.fromarray(tablica_obrazka)
# obraz_z_tablicy.show()
print("=== Informacje o obrazie ===")
print(f'Tryb: {obraz_z_tablicy.mode}')
print(f'Format: {obraz_z_tablicy.format}')
print(f'Rozmiar: {obraz_z_tablicy.size}')

print(tablica_obrazka)

obraz_z_tablicy1 = tablica_obrazka.astype(np.uint8)
print(obraz_z_tablicy1)
obraz = Image.fromarray(obraz_z_tablicy1)
# obraz.show()

# Zapis tablicy obrazu do pliku
plik = open('inicjaly.txt', 'w')
for rows in tablica_obrazka_bin:
    for item in rows:
        plik.write(str(item) + ' ')
    plik.write('\n')
plik.close()


print('\n=== Zadanie 4 ===')
piksel_63_31 = tablica_obrazka_bin[31][63]
print(f'(63,31) = {piksel_63_31}')
piksel_50_30 = tablica_obrazka_bin[30][50]
print(f'(50,30) = {piksel_50_30}')
piksel_90_40 = tablica_obrazka_bin[40][90]
print(f'(90,40) = {piksel_90_40}')
piksel_99_0 = tablica_obrazka_bin[0][99]
print(f'(99,0) = {piksel_99_0}')


print('\n=== Zadanie 5 ===')
txt_as_bool = np.loadtxt('inicjaly.txt', dtype=np.bool_)
print('=== Informacje bool_ ===')
print(f'Typ danych tablicy: {txt_as_bool.dtype}')
print(f'Rozmiar: {txt_as_bool.shape}')
print(f'Wymiar: {txt_as_bool.ndim}')
print('\n=== Informacje bmp ===')
print(f'Typ danych tablicy: {tablica_obrazka.dtype}')
print(f'Rozmiar: {tablica_obrazka.shape}')
print(f'Wymiar:  {tablica_obrazka.ndim}')
czy_rowne = np.array_equal(txt_as_bool, tablica_obrazka)
print(f'Czy równe? {czy_rowne}')


print('\n=== Zadanie 6 ===')
txt_as_uint8 = np.loadtxt('inicjaly.txt', dtype=np.uint8)
print('=== Informacje uint8_ ===')
print(f'Typ danych tablicy: {txt_as_uint8.dtype}')
print(f'Rozmiar: {txt_as_uint8.shape}')
print(f'Wymiar:  {txt_as_uint8.ndim}')
obraz_z_tablicy_uint8 = Image.fromarray(txt_as_uint8)
# obraz_z_tablicy_uint8.show()
# a) zmienił się typ danych tablicy
# b) Jest ledwie widoczny, bo różnica 0 a 1 jest mała, mamy 8 bit na kolor czyli 0-255


print('\n=== Zadanie 7 ===')
obrazek_16 = Image.open('inicjaly16.bmp')
print("=== Informacje o obrazie 16-kolor ===")
print(f'Tryb: {obrazek_16.mode}')
print(f'Format: {obrazek_16.format}')
print(f'Rozmiar: {obrazek_16.size}')
tablica_obrazka_16 = np.asarray(obrazek_16)
print(f'Typ danych tablicy: {tablica_obrazka_16.dtype}')
print(f'Rozmiar: {tablica_obrazka_16.shape}')
print(f'Wymiar: {tablica_obrazka_16.ndim}')

obrazek_256 = Image.open('inicjaly256.bmp')
print("\n=== Informacje o obrazie 256-kolor ===")
print(f'Tryb: {obrazek_256.mode}')
print(f'Format: {obrazek_256.format}')
print(f'Rozmiar: {obrazek_256.size}')
tablica_obrazka_256 = np.asarray(obrazek_256)
print(f'Typ danych tablicy: {tablica_obrazka_256.dtype}')
print(f'Rozmiar: {tablica_obrazka_256.shape}')
print(f'Wymiar: {tablica_obrazka_256.ndim}')

obrazek_24bit = Image.open('inicjaly24bit.bmp')
print("\n=== Informacje o obrazie 24-bit ===")
print(f'Tryb: {obrazek_24bit.mode}')
print(f'Format: {obrazek_24bit.format}')
print(f'Rozmiar: {obrazek_24bit.size}')
tablica_obrazka_24bit = np.asarray(obrazek_24bit)
print(f'Typ danych tablicy: {tablica_obrazka_24bit.dtype}')
print(f'Rozmiar: {tablica_obrazka_24bit.shape}')
print(f'Wymiar: {tablica_obrazka_24bit.ndim}')

obrazek_jpg = Image.open('inicjaly.jpg')
print("\n=== Informacje o obrazie jpg ===")
print(f'Tryb: {obrazek_jpg.mode}')
print(f'Format: {obrazek_jpg.format}')
print(f'Rozmiar: {obrazek_jpg.size}')
tablica_obrazka_jpg = np.asarray(obrazek_jpg)
print(f'Typ danych tablicy: {tablica_obrazka_jpg.dtype}')
print(f'Rozmiar: {tablica_obrazka_jpg.shape}')
print(f'Wymiar: {tablica_obrazka_jpg.ndim}')
# Bialy
# print(f'{tablica_obrazka_jpg[40][90][0]}')
# print(f'{tablica_obrazka_jpg[40][90][1]}')
# print(f'{tablica_obrazka_jpg[40][90][2]}')
# Czarny
# print(f'{tablica_obrazka_jpg[30][50][0]}')
# print(f'{tablica_obrazka_jpg[30][50][1]}')
# print(f'{tablica_obrazka_jpg[30][50][2]}')

obrazek_png = Image.open('inicjaly.png')
print("\n=== Informacje o obrazie png ===")
print(f'Tryb: {obrazek_png.mode}')
print(f'Format: {obrazek_png.format}')
print(f'Rozmiar: {obrazek_png.size}')
tablica_obrazka_png = np.asarray(obrazek_png)
print(f'Typ danych tablicy: {tablica_obrazka_png.dtype}')
print(f'Rozmiar: {tablica_obrazka_png.shape}')
print(f'Wymiar: {tablica_obrazka_png.ndim}')

# Tryb P - paleta kolorów, każdy kolor ma przyporządkowany inny numer
# Tryb RGB - kolor zapisany jako składowe R (red), G (green), B (blue)
# Tryb RGBA - kolor zapisany jako składowe R (red), G (green), B (blue), A (alpha)
# 16-kolor ma 0-15, 256-kolor ma 0-255
# Wymiar 2 szerokość i wysokość, 3 to kanały kolorów
