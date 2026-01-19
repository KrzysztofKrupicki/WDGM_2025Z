import math

import matplotlib.pyplot as plt
import numpy as np
from PIL import (
    Image,
    ImageChops,
    ImageColor,
    ImageDraw,
    ImageFilter,
    ImageFont,
    ImageOps,
)
from PIL import ImageStat as stat

"""========== Zadanie 1 ==========
1. Mieszanie obrazów.
    a. Wybierz dwa obrazy obraz1 i obraz2 w trybie RGB i tych samych rozmiarów. (Jeśli obrazy nie spełniają tych wymagań zastosuj convert i/lub resize.)
    b. Zmieszaj obraz1 z obrazem2 w proporcji 2:3
"""
obraz1 = Image.open("amvalkyrie.png").convert("RGB")
obraz2 = Image.open("amvantage.png").convert("RGB")
result = Image.blend(obraz1, obraz2, 0.6)
result.save("result1.png")
# result.show()


"""========== Zadanie 2 ==========
2. Wycinanie i wklejanie.
    a. Wytnij z obrazu1 wybrany fragment i wklej w wybrane miejsce w obrazie2.
    b. Utwórz obraz maska tych samych rozmiarów co obrazy 1 i 2, zawierający białą elipsę z wypełnieniem na czarnym tle. Elipsę należy wpisać w box użyty w pkt.2a do wycięcia fragmentu. Pamiętaj, że maska może być tylko w określonych trybach
    c. Wklej obraz2 w obraz1 z maską maska.
    d. Wklej obraz1 w obraz2 z maską maska.
    e. Dodaj do obrazu1 obraz maska jako kanał alpha 
"""
box = (100, 100, 400, 300)  # (lewo, góra, prawo, dół)
fragment = obraz1.crop(box)
obraz2_copy = obraz2.copy()
obraz2_copy.paste(fragment, (100, 100))
obraz2_copy.save("result2.png")
# obraz2.show()

"""
b. Utwórz obraz maska tych samych rozmiarów co obrazy 1 i 2, zawierający białą elipsę z wypełnieniem na czarnym tle. Elipsę należy wpisać w box użyty w pkt.2a do wycięcia fragmentu. Pamiętaj, że maska może być tylko w określonych trybach
"""
maska = Image.new("L", obraz1.size, 0)
draw = ImageDraw.Draw(maska)
draw.ellipse(box, fill=255)
maska.save("maska.png")

"""
c. Wklej obraz2 w obraz1 z maską maska.
"""
obraz1_copy = obraz1.copy()
obraz1_copy.paste(obraz2, (0, 0), maska)
obraz1_copy.save("result3.png")

"""
d. Wklej obraz1 w obraz2 z maską maska.
"""
obraz2_copy = obraz2.copy()
obraz2_copy.paste(obraz1, (0, 0), maska)
obraz2_copy.save("result4.png")

"""
e. Dodaj do obrazu1 obraz maska jako kanał alpha 
"""
obraz1.putalpha(maska)
obraz1.save("result5.png")


"""========== Zadanie 3 ==========
3. Wstawianie tekstu do obrazu.
    a. Dodaj tekst "Jedi używa Mocy do zdobywania wiedzy i obrony, nigdy do ataku" do obrazu1 w następujący sposób:
        i. Wielkość czcionki powinna być maksymalna, ale taka, żeby tekst zmieścił się w 3 linijkach
        ii. Rodzaj czcionki, to DejaVuSansDisplay.ttf
        iii. Kolor liter, to chartreuse
    b. Dodaj tekst jak w 3a. stosując przezroczystość 200
"""
base = Image.open("amvantage.png").convert("RGB")
fnt = ImageFont.truetype("ttf/DejaVuSans-BoldOblique.ttf", 42)
draw = ImageDraw.Draw(base)
tekst = "Jedi używa Mocy do zdobywania\nwiedzy i obrony,\nnigdy do ataku"
draw.text((40, 40), tekst, font=fnt, fill=(127, 255, 0), align="left")
base.save("result6.png")

"""
b. Dodaj tekst jak w 3a. stosując przezroczystość 200
"""
base = Image.open("amvalkyrie.png").convert("RGBA")
txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
fnt = ImageFont.truetype("ttf/DejaVuSans-BoldOblique.ttf", 42)
draw = ImageDraw.Draw(base)
tekst = "Jedi używa Mocy do zdobywania\nwiedzy i obrony,\nnigdy do ataku"
draw.text((40, 40), tekst, font=fnt, fill=(255, 0, 255, 200), align="left")
out = Image.alpha_composite(base, txt)
out.save("result7.png")


"""========== Zadanie 4 ==========
4. Wstawianie figur geometrycznych.
    a. Utwórz obraz o rozmiarach 200x100 w trybie RGB w kolorze blue.
        i. Narysuj na obrazie dwa okręgi styczne do siebie i krawędzi obrazu
            1. Okrąg po lewej stronie bez wypełnienia, kolor krawędzi #ff69b4, grubość krawędzi 5
            2. Okrąg po prawej stronie z tymi samymi parametrami, ale w kolorze negatywu okręgu lewego
    b. Na obrazie1 narysować dwa czarne kwadraty (bez wypełnienia) w takim położeniu jak obok (tzn. każdy kwadrat dotyka brzegów obrazu w trzech punktach)
"""
img_geo = Image.new("RGB", (200, 100), "blue")
draw = ImageDraw.Draw(img_geo)
color_left = "#ff69b4"
color_right = (0, 150, 75)
draw.ellipse([0, 0, 100, 100], outline=color_left, width=5)
draw.ellipse([100, 0, 200, 100], outline=color_right, width=5)
img_geo.save("result8.png")

"""
b. Na obrazie1 narysować dwa czarne kwadraty (bez wypełnienia) w takim położeniu jak obok (tzn. każdy kwadrat dotyka brzegów obrazu w trzech punktach)
"""
img1 = Image.open("amvantage.png").convert("RGB")
draw1 = ImageDraw.Draw(img1)
w, h = img1.size
romb_lewy = [
    (0, h / 2),
    (h / 2, 0),
    (h, h / 2),
    (h / 2, h),
]
draw1.polygon(romb_lewy, outline="black", width=5)
romb_prawy = [
    (w - h, h / 2),
    (w - h / 2, 0),
    (w, h / 2),
    (w - h / 2, h),
]
draw1.polygon(romb_prawy, outline="black", width=5)
img1.save("result9.png")
