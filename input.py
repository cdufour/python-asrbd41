# input.py
print("Combien d'étudiants attendus ?")
nbStudentsMax = input()

print("Combien d'étudiants présents ?")
nbStudents = input()
print(nbStudents + " étudiants sont présents")

# Si le nombre d'étudiants présent est supérieur
# à la moitié du nombre d'étudiants attendu,
# le cours aura lieu, sinon: il est annulé
if (int(nbStudents) > int(nbStudentsMax) / 2):
    print('Cours maintenu')
else:
    print('Cours annulé')
