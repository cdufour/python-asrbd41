# sumList2.py
notesStudent1 = [2, 18, 13, 7, 14]
notesStudent2 = [20, 16, 13, 18, 18.5]
notesStudent3 = [5, 3, 7, 8, 10]

# liste de listes
students = [notesStudent1, notesStudent2, notesStudent3]

# Calculer et afficher la somme grâce à une fonction
# afin d'éviter une reproduction (copier-coller)
# de code inutile/inélégante/inefficace

def listAverage(values):
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)

for student in students:
    print(listAverage(student))
