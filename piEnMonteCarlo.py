import random


tir = 1
NbTirsDqnsLeDisque = 0

while (tir < 10000):
    tir += 1
    # On tire au hasard un point du quart de carre [0, 1] * [0,1]
    x = random.random()
    y = random.random()
    # On compte le nombre de fois ou l'on est dans le disque.
    if (x**2 + y**2 <= 1):
        NbTirsDqnsLeDisque += 1

""" la probabilite que le point tire au hasard soit dans
le quart  du disque est egale a l'aire du quart du 
cercle sur l'aire du carre soit pi/4.

"""

pi = 4*NbTirsDqnsLeDisque / tir
print("Valeur experimentale de pi : %0.3f" %pi)