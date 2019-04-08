# majority.py

# Ecrire un programme demandant à l'utilisateur
# de saisir son âge
# s'il est supérieur à 17, on affiche "tu peux passer le permis"
# s'il est compris entre 16 (inclus) et 18 (non inclus) => "Conduite acc. possible"
# s'il est inférieur à 16 => "Tu dois attendre"
print('Ton âge ?')
age = input()

# bonne solution, on n'évalue pas systématiquement toutes le possibilités
if int(age) > 17:
    print("Tu peux passer le permis")
else:
    if int(age) >= 16:
        print("Conduite accompagnée possible")
    else:
        print("Tu dois attendre...")

# Variante "sale" (plus gourmande en performance)
# tous les if sont traités par python même lorsque ce
# n'est pas nécessaire (les conditions s'excluent mutuellement)
if int(age) > 17:
    print("Tu peux passer le permis")

if int(age) >= 16 and int(age) < 18:
    print("Conduite accompagnée possible")

if int(age) < 16:
    print("Tu dois attendre...")
