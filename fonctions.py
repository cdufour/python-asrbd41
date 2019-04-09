# fonctions.py

def bonjour():
    print('Bonjour, je suis courtois')
    # retourne la valeur None de manière implicite

def bonjourMult(nb):
    while nb > 0:
        print('Bonsoir, je suis courtois')
        nb -= 1

def sum(v1, v2):
    # print(v1 + v2)
    return v1 + v2

# bonjour()
# bonjourMult(3)

total = sum(16,13)
print(total)

# Créer une fonction multiply qui renvoie
# le produit de deux valeurs fournies en
# entrée de cette fonction

def multiply(v1, v2):
    return v1 * v2

# Créer une fonction square qui renvoie
# le carré d'un nombre fourni en entrée
def square(nb):
    return nb*nb

# print(square(2+2)) équivalent de: square(4)

values = [4,5,6]
for value in values:
    print('Carre de ' + str(value) + ': ' + str(square(value)))

# Créer une fonction qui prend en entrée un tableau de nombres
# et renvoie la moyenne des nombres
def listAverage(values):
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)

print(listAverage([7,9,65])) # output: 27.0

print('bonjour', 'ciao')
