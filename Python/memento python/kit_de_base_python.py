# kit de base pour python
# Quand on débute ou qu'on oublie.
# tout ce qui suit un dièse est un commentaire et ignoré de python
######################################################################
# Variables
######################################################################
# définition de variable
x = 0
# plusieurs variables
a,b = 0,1 # -> a vaut 0 et b vaut 1
# nuplets (tuples)
x = (0,1)
a,b = x # -> a vaut 0 et b vaut 1
# modifier une variable globale dans une fonction
def f(c) :
    global a
    a = a + b # on peut modifier a car elle a été déclarée globale
              # on peut lire b mais pas la modifier
    return(c+b)

f(3) # -> 4, et a vaut maintenant 1
######################################################################
# Nombres
######################################################################
# entiers
1024 # 2^10
# flottants
3.14159e20 # pi * 10^20
# partie entière
int(3.14) # -> 3
# opérations
3+5-2*3 # -> 2
# division
4/7 # -> 0.5714285714285714
# division entière
9//4 # -> 2
# modulo
9%4 # -> 1
# puissance
3**4 # -> 81
######################################################################
# Fonctions
######################################################################
#définition de fonction
def f(x,y):
    res = x**2+y+1
    return(res)

f(2,3) # -> 8

######################################################################
# If, branchements
######################################################################
if (x == 0 or x == 2) and (x<4):
    x = x + 1
elif x!= 1:
    x = 3
else:
    x = 0
######################################################################
# Boucles for, range
######################################################################
for i in range(5) :
    print(i) 
# -> 0 1 2 3 4
for i in range(2,6) :
    print(i) 
# -> 2 3 4 5
for i in range(4,12,2) :
    print(i, "", end = "") # pour ne pas aller à la ligne
# -> 4 6 8 10
# en utilisant une liste (ou un nuplet)
for i in [0,4,3,2,6] :
    print(i) 
# -> 0 4 3 2 6
######################################################################
# Nuplets (= tuples)
######################################################################
# un nuplet à 3 éléments
x = (4,"a",2)
# accéder à un élément: les indices commencent à 0
x[0] # -> 4
# un nuplet à 1 seul élément
x = (0,)
# on ne peut pas modifier un nuplet !
x[0] = 1 # ERREUR
# concaténation de nuplets
(0,1)+(2,3) # -> (0,1,2,3)
# créer un nuplet à partir d'un itérable(liste, range)
tuple([0,1,2]) # -> (0,1,2)
tuple(range(4)) # -> (0,1,2,3)
######################################################################
# Listes (tableaux)
######################################################################
# une liste à 3 éléments
x = [4,"a",2]
# accéder à un élément
x[0] # -> 4
# en partant de la fin
x[-1] # -> 2
# liste vide
[]
# longueur d'une liste
len([2,3,4,5]) # -> 4
# on peut modifier une liste !
x[0] = 1 # -> x vaut [1,"a",2]
# concaténation de listes
[0,1]+[2,3] # -> [0,1,2,3]
# créer une liste à partir d'un itérable
list((0,1,2)) # -> [0,1,2]
list(range(4)) # -> [0,1,2,3]
# ajouter un élément à la fin
x = [0,1]
x.append(2)
x # -> [0,1,2]
# enlever le dernier élément
x.pop() # -> 2
x # -> [0,1]
# Liste en compréhension
[i for i in range(4)] # -> [0,1,2,3]
[i*i for i in range(4)] # -> [0,1,4,9]
[i*i+1 for i in range(5) if i != 2] # -> [1,2,10,17]
# matrices 3x3, les indices commencent à 1
A = [[i+j for j in range(3)] for i in range(3)]
# A vaut [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
A[1][2] # -> 3
A[1][2] = 4 # A est modifiée: A[1][2] vaut 4
# sous-liste
x = [i for i in range(12)]
y = x[2:6] # -> [2,3,4,5]
y = x[8:] # -> [8,9,10,11]
y = x[:4] # -> [0,1,2,3]
# copie d'une liste
y = x[:]
y[0] = 10 # ne modifie pas x

######################################################################
# Chaînes de caractères
######################################################################
# nouvelle chaîne
s = 'tutu'
s2 = "titi"
s3 = """
un long texte avec des retours à la ligne
et tout ce qu'on veut
"""
# retour à la ligne
"\n"
# concaténation
"tu"+"tu" # -> "tutu"
# sous-chaîne
x = "tutu"
x[0] # -> "t"
x[0:2] # -> "tu"
# transformer en chaîne
str(34+55) # -> '89'
# formatage de nombres
"res = {:3d}".format(32) # 3 chiffres affichés -> 'res =  32'
"res = {:3x}".format(24) # 24 en base 16 -> 'res =  18' 
"res = {:+2d} ou {:d}".format(16,17) # -> 'res = +16 ou 17'
######################################################################
# Bibliothèques
######################################################################
# pour accéder à une bibliothèque
import math
# pour accéder à une valeur dans une bibliothèque
from math import cos
# pour accéder à tout dans une bibliothèque
from math import *
# en python, les objets ont des méthodes.
# pour voir la liste des champs d'un objet
dir([]) # la liste des méthodes d'une liste
dir(1) # la liste des méthodes d'un entier
# foctions mathématiques
import math
dir(math) # la liste des valeurs dans le module math
