# fonctions.py

def bonjour():
    print('Bonsoir, je suis courtois')

def bonjourMult(nb):
    while nb > 0:
        print('Bonsoir, je suis courtois')
        nb -= 1

def sum(v1, v2):
    # print(v1 + v2)
    return v1 + v2

bonjour()
bonjourMult(3)
print(sum(7, 5))
