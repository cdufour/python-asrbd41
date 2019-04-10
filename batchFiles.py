# batchFiles.py
import os

# files = ['fichier1.txt', 'fichier2.txt', 'fichier3.txt']
files = os.listdir('./files') # équivalent à l'instruction manuelle précédente
for file in files:
    print('*** traitement de: ' + file + ' ***')

    # Lecture et remplacement
    path = './files/' + file
    f = open(path, 'r')
    content = f.read()
    newContent = content.replace('Hollande', 'Macron')
    f.close()

    # Ecriture
    f = open(path, 'w')
    f.write(newContent)
    f.close()
    print("=> SUCCESS")
