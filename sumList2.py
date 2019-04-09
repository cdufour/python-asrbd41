# sumList2.py
notesStudent1 = [2, 18, 13, 7, 14]
notesStudent2 = [20, 16, 13, 18, 18.5]
notesStudent3 = [5, 3, 7, 8, 10]
# Calculer et afficher la somme
sum = 0
for note in notesStudent1:
    sum += note
print('Somme des notes: ' + str(sum))

# Calculer et afficher la moyenne
average = sum / len(notesStudent1)
print('Moyenne des notes: ' + str(average))

# Pour afficher la moyenne des autres étudiants
# EVITER le copier-coller du code précédent
# Solution: utiliser une fonction
