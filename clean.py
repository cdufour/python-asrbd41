# clean.py

'''
Ecrire un programme devant itérer sur le dossier "nodanger".
Le dossier cible contient des fichiers .png, .txt et.log
Les fichiers .png seront déplacés dans un sous-dossier "png"
Les fichiers .log seront déplacés dans un sous-dossier "log"
Les fichiers .txt seront supprimés
'''
# mkdir, rename, unlink, 'samba.txt'.endswith('.txt')
import os
import datetime
target = './nodanger'

# os.mkdir(target) # error si dossier existe déjà
os.makedirs(target + '/log', exist_ok=True) # création du sous-dossier log
os.makedirs(target + '/png', exist_ok=True) # création du sous-dossier log

log = open('clean.log', 'a') # création d'un fichier permettant de tenir
# le registrer des fichiers supprimés

# on récupère et formate la date
datenow = datetime.datetime.now()
datenowformatted = datenow.strftime('%d-%m-%Y %H:%M:%S')

for file in os.listdir(target):
    if file.endswith('.log'):
        os.rename(target + '/' + file, target + '/log/' + file)
    elif file.endswith('.png'):
        os.rename(target + '/' + file, target + '/png/' + file)
    elif file.endswith('.txt'):
        os.unlink(target + '/' + file)
        absPath = os.path.abspath(target + '/' + file)
        log.write(datenowformatted + '\t' + absPath + ' DELETED\n')
    else:
        None # on ne fait rien si l'on traite un fichier d'une autre extension

log.close()
