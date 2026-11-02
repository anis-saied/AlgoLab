"""
exercice 4 page 20 (cinématique): mon livre physique de terminale C
"""
from math import sqrt


print("it works")
# vecteur acceleration constant de valeur algébrique A= -2 m/s²
A = -2

# valeur algébrique de vecteur vitesse à t=0 est v= 10 m/s
v0 = 10

# à t=0, le mobile est à l'origine des abscisses, x0 = 0 à t=0
x0 = 0

"""
rappel :
si A = constante 
Alors
v = At + v0  
et
x = 1/2 A t² + V0 t + x0
"""
# Structure de données, 
"""
d [x][date]=vitesse
le mobile peut passer par chaque abscisse, plusieurs fois
à des instantes différents avec des vitesses différentes
d = {
    0: {
        0: 10,
        10:-10
    },
    -11: {
        -1 : 12,
        11:-12
    },
}
"""
d=dict()
d[0]={0:10}
# date et abscisse d'annulation de vecteur vitesse (et changement de sens)
# v= At + v0 , vitsse s'annule ,donc 0 = At+v0, donc, t = -v0/A
t_annulation_vitesse = - v0 / A
x_annulation = (1/2)*A*(t_annulation_vitesse**2) + v0 *t_annulation_vitesse + x0
d[x_annulation]={t_annulation_vitesse:0}
output = f"""
t_annulation_vitesse = {t_annulation_vitesse} s
x_annulation  = {x_annulation} m/s
"""
print(output)
print(d)

# Question : les dates et les valeurs algébriques des vitesses
# correspondant aux abscisses : 0, 9, -11
abscisses = (0, 9, -11)

def vitesse(x,A,v0):
    # v²- v0² = 2Ax   ---->     v = (+-) racine(2Ax + v0²)
    v = sqrt(2*A*x + v0**2)
    print("x=",x,"v=",v)
    return v, -v

def date(v,v0, A):
    # v = At + v0   ----> t = (v-v0)/A
    t = (v-v0)/A
    print("t=",t,"v=",v)
    return t

dates = []
for x in abscisses:
    print("-"*20)
    vitesses = vitesse(x,A,v0)
    d[x]={}
    for v in vitesses:
        t=date(v,v0,A)
        d[x][t]=v
print("-"*20)
print(d)