from PIL import Image, ImageFilter, ImageOps
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageStat as stat


def statystyki(im):
    print("tryb obrazu", im.mode)
    print("rozmiar obrazu", im.size)
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

"""========== Zadanie 1 ==========
Zastosuj metode resize do obrazu postac. Utwórz 6 obrazów przyjmując skalę dla szerokości s_w = 0.15, skalę dla wysokości s_h = 0.27 oraz kolejno metody resamplingu 'NEAREST','LANCZOS','BILINEAR','BICUBIC','BOX','HAMMING' Przedstaw na jednym diagramie plt (fig1.png) obrazy po przeskalowaniu i ich różnice w stosunku do NEAREST. Pobierz statystyki różnic i skomentu
"""

im = Image.open("postac.jpg")
s_w = 0.15
s_h = 0.27
w, h = im.size
w0 = int(w * s_w)
h0 = int(h * s_h)

im_NEAREST = im.resize((w0, h0), resample=0, reducing_gap=None)
diff_NEAREST = ImageChops.difference(im_NEAREST, im_NEAREST)
print("Statystyki dla różnicy obrazów NEAREST i NEAREST:")
stat_diff_NEAREST = statystyki(diff_NEAREST)
im_LANCZOS = im.resize((w0, h0), resample=1, reducing_gap=None)
diff_NEAREST_LANCZOS = ImageChops.difference(im_NEAREST, im_LANCZOS)
print("Statystyki dla różnicy obrazów NEAREST i LANCZOS:")
stat_diff_NEAREST_LANCZOS = statystyki(diff_NEAREST_LANCZOS)
im_BILINEAR = im.resize((w0, h0), resample=2, reducing_gap=None)
diff_NEAREST_BILINEAR = ImageChops.difference(im_NEAREST, im_BILINEAR)
print("Statystyki dla różnicy obrazów NEAREST i BILINEAR:")
stat_diff_NEAREST_BILINEAR = statystyki(diff_NEAREST_BILINEAR)
im_BICUBIC = im.resize((w0, h0), resample=3, reducing_gap=None)
diff_NEAREST_BICUBIC = ImageChops.difference(im_NEAREST, im_BICUBIC)
print("Statystyki dla różnicy obrazów NEAREST i BICUBIC:")
stat_diff_NEAREST_BICUBIC = statystyki(diff_NEAREST_BICUBIC)
im_BOX = im.resize((w0, h0), resample=4, reducing_gap=None)
diff_NEAREST_BOX = ImageChops.difference(im_NEAREST, im_BOX)
print("Statystyki dla różnicy obrazów NEAREST i BOX:")
stat_diff_NEAREST_BOX = statystyki(diff_NEAREST_BOX)
im_HAMMING = im.resize((w0, h0), resample=5, reducing_gap=None)
diff_NEAREST_HAMMING = ImageChops.difference(im_NEAREST, im_HAMMING)
print("Statystyki dla różnicy obrazów NEAREST i HAMMING:")
stat_diff_NEAREST_HAMMING = statystyki(diff_NEAREST_HAMMING)



plt.figure(figsize=(16, 12))
plt.subplot(2, 6, 1)
plt.title("im_NEAREST")
plt.imshow(im_NEAREST)
plt.axis("off")
plt.subplot(2, 6, 7)
plt.title("diff_NEAREST")
plt.imshow(diff_NEAREST)
plt.axis("off")
plt.subplot(2, 6, 2)
plt.title("im_LANCZOS")
plt.imshow(im_LANCZOS)
plt.axis("off")
plt.subplot(2, 6, 8)
plt.title("diff_NEAREST_LANCZOS")
plt.imshow(diff_NEAREST_LANCZOS)
plt.axis("off")
plt.subplot(2, 6, 3)
plt.title("im_BILINEAR")
plt.imshow(im_BILINEAR)
plt.axis("off")
plt.subplot(2, 6, 9)
plt.title("diff_NEAREST_BILINEAR")
plt.imshow(diff_NEAREST_BILINEAR)
plt.axis("off")
plt.subplot(2, 6, 4)
plt.title("im_BICUBIC")
plt.imshow(im_BICUBIC)
plt.axis("off")
plt.subplot(2, 6, 10)
plt.title("diff_NEAREST_BICUBIC")
plt.imshow(diff_NEAREST_BICUBIC)
plt.axis("off")
plt.subplot(2, 6, 5)
plt.title("im_BOX")
plt.imshow(im_BOX)
plt.axis("off")
plt.subplot(2, 6, 11)
plt.title("diff_NEAREST_BOX")
plt.imshow(diff_NEAREST_BOX)
plt.axis("off")
plt.subplot(2, 6, 6)
plt.title("im_HAMMING")
plt.imshow(im_HAMMING)
plt.axis("off")
plt.subplot(2, 6, 12)
plt.title("diff_NEAREST_HAMMING")
plt.imshow(diff_NEAREST_HAMMING)
plt.axis("off")
plt.savefig("fig1.png")

"""
BOX / BILINEAR / HAMMING: Wykazują mniejsze różnice niż inne metody, ponieważ ich algorytmy są mniej agresywne w wygładzaniu krawędzi.

LANCZOS / BICUBIC: Generują największe różnice względem NEAREST. Wynika to z faktu, że algorytmy te stosują zaawansowaną interpolację, która wygładza krawędzie (antyaliasing), podczas gdy NEAREST pozostawia ostre, schodkowane piksele.
"""

"""========== Zadanie 2 ==========
Porównaj dwa obrazy (statystyki różnicy) otrzymane w następujący sposób:
    a. Stosując metodę resize z wybraną metodą resamplingu powiększ fragment obraz postac przedstawiający głowę dwukrotnie na szerokość i trzykrotnie na wysokość
    b. Stosując metodę crop wytnij ten sam fragment obrazu postac i otrzymany obraz powiększ dwukrotnie z tą samą metodą resmplingu na szerokość i trzykrotnie na wysokość
"""
glowa = (250, 0, 550, 300)
glowa_crop = im.crop((250, 0, 550, 300))
w, h = glowa_crop.size
new_w = w * 2
new_h = h * 3
glowa_crop_resize = im.crop((glowa)).resize(
    (new_w, new_h), resample=Image.Resampling.LANCZOS)
glowa_crop_resize.save('glowa_crop_resize.png')
glowa_resize = im.resize(
    (new_w, new_h), resample=Image.Resampling.LANCZOS, box=glowa)
glowa_resize.save('glowa_resize.png')
diff_resize = ImageChops.difference(glowa_crop_resize, glowa_resize)
diff_resize.save('diff_resize.png')


plt.figure(figsize=(12, 6))
plt.subplot(1, 4, 1)
plt.title("Fragment")
plt.imshow(glowa_crop)
plt.axis("off")
plt.subplot(1, 4, 2)
plt.title("Powiększony (resize)")
plt.imshow(glowa_resize)
plt.axis("off")
plt.subplot(1, 4, 3)
plt.title("Powiększony (crop + resize)")
plt.imshow(glowa_crop_resize)
plt.axis("off")
plt.subplot(1, 4, 4)
plt.title("diff imageChops")
plt.imshow(diff_resize)
plt.axis("off")
# plt.show()
plt.savefig("fig_crop_resize.png")


"""========== Zadanie 3 ==========
Obróć obraz
    a. o 60 stopni w lewo dobierając argumenty metody rotate tak, żeby widoczny był cały obraz postac, a nadmiarowy fragment był w kolorze czerwonym
    b. o 60 stopni w prawo dobierając argumenty metody rotate tak, żeby rozmiar obrazu postac się nie zmienił, a nadmiarowy fragment był w kolorze zielonym
"""
obrot_l = im.rotate(60, expand=True, fillcolor='red')
obrot_l.save('obrot_l.png')
obrot_p = im.rotate(-60, expand=False, fillcolor='green')
obrot_p.save('obrot_p.png')


"""========== Zadanie 4 ==========
Parametr expand nie działa dobrze, gdy center nie jest środkiem obrazu. Zaproponuj rozwiązanie, które pozwoli dokonać obrotu obrazu wokół punktu (0,0) tak, żeby widoczny był cały obraz. Wynik zapisz jako obraz obrot.png Wskazówka: stworzyć nowy obraz o wymiarach takich, żeby punkt obrotu był jego środkiem.

"""

def obrot_wokol_0_0(obraz, kat):
    w, h = obraz.size
    new_im = Image.new(obraz.mode, (w*2, h*2), (0, 0, 0, 0) if obraz.mode == 'RGBA' else (0, 0, 0))
    new_im.paste(obraz, (w, h))
    return new_im.rotate(kat, expand=True)


obrot_wokol_0_0(im, 60).save('obrot.png')




"""========== Zadanie 5 ==========
Czy przekształcenia Image.TRANSPOSE i Image.TRANSVERSE można otrzymać wykonując obroty i Image.FLIP_LEFT_RIGHT? Jeśli tak, napisz jak to zrobić
"""

"""
Oba przekształcenia można uzyskać za pomocą obrotu i odbicia lustrzanego: 
Image.TRANSPOSE (odbicie względem głównej przekątnej, zamiana x na y): Wykonaj obrót o 270 stopni w lewo (lub 90 w prawo) i Image.FLIP_LEFT_RIGHT.
Image.TRANSVERSE (odbicie względem drugiej bocznej): Wykonaj obrót o 90 stopni w lewo i Image.FLIP_LEFT_RIGHT.
"""


def manual_transpose(img):
    # TRANSPOSE: Odbicie względem głównej przekątnej. Zamiana osi X i Y
    # Można to uzyskać obracając o 90 stopni w prawo i odbijając w poziomie
    return img.rotate(-90).transpose(0) # 0 = FLIP_LEFT_RIGHT
    # return img.transpose(5) # 5 = TRANSPOSE

manual_transpose(im).show()
manual_transpose(im).save('transpose.png')


def manual_transverse(img):
    # TRANSVERSE: Odbicie względem drugiej przekątnej
    # Można to uzyskać obracając o 90 stopni w lewo i odbijając w poziomie
    return img.rotate(90).transpose(0) # 0 = FLIP_LEFT_RIGHT
    # return img.transpose(6) # 6 = TRANSVERSE


manual_transverse(im).show()
manual_transverse(im).save('transverse.png')


"""========== Zadanie 6 ==========
Z obrazu motylek.png utwórz maskę o takich wymiarach, by na wybranym obrazie postac estetycznie wkleić trzy motylki (w normalnym położeniu, obrócony o 60 stopni w prawo, obrócony o 60 stopni w lewo). Skorzystaj z wklejania z maską obrazu kolorowe_tlo.png w obraz postac. Uwaga: można korzystać z resize, rotate i convert.
"""


def create_custom_mask(source_path, threshold):
    m_img = Image.open(source_path)
    r_chan = m_img.split()[0]
    mask = r_chan.point(lambda x: 255 if x < threshold else 0)
    for _ in range(2):
        mask = mask.filter(ImageFilter.MaxFilter(3))
    for _ in range(2):
        mask = mask.filter(ImageFilter.MinFilter(3))
    return mask


motylek_mask = create_custom_mask('motylek.png', 255)
tlo = Image.open('kolorowe_tlo.png').resize((120, 120))
postac_final = im.copy()
motylki_cfg = [(0, (70, 350)), (-60, (170, 120)), (60, (550, 130))]

for angle, pos in motylki_cfg:
    m = motylek_mask.resize((120, 120)).rotate(angle, expand=True, fillcolor=0)
    t = tlo.rotate(angle, expand=True, fillcolor=0)
    postac_final.paste(t, pos, m)

postac_final.save('postac_z_motylkami.png')
