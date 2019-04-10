# strings.py

message = 'Ciao tutti'
client = 'Adbel Vincent'
clients = [
    'zinédine zidane',
    'paul pogba',
    'paolo dybala'
]
# print(len(message))
# print(message[0])

# for letter in message:
    # print(letter)

# password = input('Mot de passe: ')
# if len(password) >= 3 and len(password) <= 6:
#     print('ok')
# else:
#     print('la longueur du mdp doit être comprise entre 3 et 6')

# print(message.isnumeric())
# print(message.upper())
# c = client.split(' ')
# print('Prénom:' + c[0])
# print('Nom:' + c[1].upper())

# for client in clients:
#     c = client.split(' ')
#     print("*********************")
#     print('Prenom: ' + c[0].capitalize())
#     print('Nom: ' + c[1].upper())

print(message)
# .replace renvoie une copie modifiée de la chaîne d'origine
messageModif = message.replace('tutti', 'nessuno')
print(message)



#
