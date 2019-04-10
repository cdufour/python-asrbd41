# test.py
import os
# files = os.listdir('./files')
# print(files)

# print(os.getcwd())

# fruits = ['citron', 'orange', 'cerise']
# for fruit in fruits:
    # os.mkdir(fruit) # crée le dossier
    # os.rmdir(fruit) # supprime le dossier

files = os.listdir('./files')
#for file in files:
    #os.rename(file)
os.rename('./files/' + files[0], './files/blabla.txt')




#
