# -*- coding: utf-8 -*-

import math
from fractions import Fraction
import random

a = math.pow(5,2) #renvoie toujours un flottant
b = 5**2 #renvoie un entier si possible
c = math.sqrt(25)
d = math.fabs(-3)
e = math.degrees(3.14)
f = math.radians(360)
g = math.ceil(2.3)
h = math.floor(5.8)
i = math.trunc(9.5)

un_demi = Fraction(1,2)
un_demi2 = Fraction.from_float(0.5)
j = float(un_demi)
un = un_demi+ un_demi #calcul exact contrairemnt à 0.5+0.5

k = random.random() #nombre pseudo-aléatoire entre 0 et 1
l = random.randrange(5,10,2) #renvoie un nombre aléatoire entre 5 et 10 non-inclus avec un écart de 2, donc dans la liste [5,7,9]
m = random.randint(1,6) #renvoie un nombre aléatoire entre 1 et 6
n = random.choice(['a', 'b', 'k', 'p', 'i', 'w', 'z']) #renvoie au hasard un élément d'une séquence
liste = ['a', 'b', 'k', 'p', 'i', 'w', 'z']
random.shuffle(liste) #mélange une séquence