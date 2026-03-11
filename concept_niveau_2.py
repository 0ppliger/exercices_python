## █████████████ 
## LES FONCTIONS
## █████████████ 

# -- 📕 Définition
# Une fonction :
# est un bloc de code réutilisable et paramétrable.

# Elle peut prendre des paramètres et retourner une valeur.

# Pour déclarer une fonction :
#
# def nom_de_la_fonction(nom_du_parametre: type_du_parametre) -> type_de_retour:
#     return valeur_de_retour

# eg,
def somme(notes: list) -> int:
    return 0

# Pour appeler une fonction est:
#
# nom_de_la_fonction(parametre)

total = somme([12, 14, 16])

## █████████████████ 
## LES DICTIONNAIRES
## █████████████████ 

# -- 📕 Définition
# Un dictionnaire (dict) :
# est un type qui stock un ensemble de valeur sous la forme clé -> valeur.

contact = {
    "prenom": "julien",
    "nom": "oppliger",
    "tel": "0032 2 452 487 45"
}

# Pour accéder à un élément d'un dictionnaire, on utilise la même syntaxe que
# pour une liste.

contact["prenom"]