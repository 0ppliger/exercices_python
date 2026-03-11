# Déclarez une fonction, qui prend un contact en paramètre et retourne le numéro
# de téléphone.

# un contact possède :
# - un prénom
# - un nom
# - un numéro de téléphone

contact = {
    "prenom": "julien",
    "nom": "oppliger",
    "tel": "0032 2 457 457 52"
}

def obtenir_tel(contact: dict) -> str:
    return contact["tel"]

print(obtenir_tel(contact))