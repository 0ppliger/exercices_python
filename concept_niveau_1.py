
## ███████████████ 
## LES EXPRESSIONS
## ███████████████ 

# -- 📕 Définition
# Une expression :
# est une instruction atomique évaluée par l'interpréteur.

# Il en existe plusieurs types comme :

# 👉 les expressions arithmétiques
1 + 1 

# 👉 les concaténations
"julien" + "oppliger"

# 👉 les expressions logiques
18 < 30
True and True

# 👉 les appels de fonction
print("Hello world !")

# 👉 les affectations de variable
a = 10

# 👉 et plein d'autres !
#   (déclaration de variable et de fonction, condition, boucle, etc.)

# -- 🤔 Remarque:
# Les expressions sont évaluées 
# les unes après les autres du plus 
# bas au plus haut dans la hierarchie.

# eg, :
print(pow(4 ,3 + pow(3 * 2, 4)))
print(pow(4 , 3 + pow(6, 4)))
print(pow(4 , 3 + 1296))
print(pow(4 , 1299))
print(11910465487876695589717869) # ..

## █████████████
## Les variables
## █████████████

# -- 📕 Définition
# La déclaration de variable :
# indique au système que la variable existe
a = "variable déclarée"

# -- 📕 Définition
# l' affectation de variable :
# indique au système que la variable contient cette valeur
a = "variable affectée"

# -- Remarque:
# En python la déclaration d'une variable 
# se fait au moment de l'affectation.

# La variable est déclarée lorsqu'elle est affectée pour la première fois.
b = "ma valeur" 
# Elle peut être réaffectée mais pas redéclarée.
b = "une autre valeur" 

## █████████ 
## LE TYPAGE
## █████████ 

# -- 📕 Définition
# Un type :
# détermine le type de valeur qu'une variable stock stock.

# Voici les principaux types de python:

# 👉 chaîne de caractères (str)
a = "une chaîne de caractères"
a = 'une chaîne de caractères'

# 👉 nombre entier (int)
entier = 10

# 👉 nombre flottant (float)
flottant = 10.0

# 👉 booléen (bool)
booleen = True
booleen = False

# -- 🤔 Remarque:
# Python est un langage a typage dynamique fort.
# Cela signifie qu'il ne va pas réaliser de conversion de type pour vous. Si une
# fonction attend une chaîne vous devez lui passer une chaîne.

# eg,
# age stock un entier (int)
age = 20 
# une concaténation attend des chaînes (str)
print("julien" + str(age))
# str(age) permet de convertir un type int en type str.

... (114lignes restantes)

intro.py
6 Ko
Oppliger
 — 
09/03/2026 13:52

# Déclarez une liste de note et affichez les totues sous la forme
# note = 12
# note = 15
# note = 8
# etc.
# Voici les notes à utiliser :
# 12, 15, 8, 13, 20, 7

Oppliger
 — 
09/03/2026 14:19

# Déclarez une liste de note, transformez les notes sur 20 en note sur 100 et affichez les sous la forme
# note sur 100 = 50
# etc.
# Voici les notes à utiliser :
# 10 14 12 8 7 20

 
Oppliger
 — 
09/03/2026 15:03

# Déclarez une liste de note
# 4 14 10 18 13 10

# affichez 
# 4 est en dessous de la moyenne
# 15 est au dessus de la moyenne
# 10 est à la moyenne
# 18 est au dessus de la moyenne
# 13 est au dessus de la moyenne
# 10 est à la moyenne

Oppliger
 — 
09/03/2026 15:53

# Etant donné un nombre n, affichez
# "Fizz" si le nombre est divisible par 3
# "Buzz" si le nombre est divisible par 5
# "FizzBuzz" si le nombre est divisible par 3 et 5
# Parcourez tous les nombres de 1 à 100

 
Oppliger
 — 
Hier à 08:43

Vous implémentez une API REST avec FastAPI, qui contient un endpoint :
POST /signin {username: string, password: string}
et qui retourne { success: true | false } si la pair username/password correspond à ce que vous écris en dur dans le code

Oppliger
 — 
Hier à 10:58

Étant donné une liste de notes :
14, 15, 10, 12, 8, 16, 11, 14, 19
Affichez un rapport sous la forme suivante :

Nombre de notes = 9
Note 1 = 14/20 (Très bien)
Note 2 = 15/20 (Très bien)
Note 3 = 10/20 (Passable)
Note 4 = 12/20 (Bien)
Note 5 = 08/20 (Insuffisant)
Note 6 = 16/20 (Excellent)
Note 7 = 11/20 (Passable)
Note 8 = 14/20 (Très bien)
Note 9 = 19/20 (Excellent)
Note minimale = 8
Note maximale = 19
Moyenne = 13.2 (Bien)
Delta = 11

Notes:

Delta :
C'est la différence entre la note minimale et maximale

Mentions :
16 - 20   = Excellent
14 - 15.9 = Très bien
12 - 13.9 = Bien
10 - 11.9 = Passable
00 - 9.9  = Insuffisant

 
Oppliger
 — 
Hier à 11:09

Développez un outil de fuzzing.
voilà comment utiliser l'outil:

Pour réaliser une attaque de brute force :
$ h4cktool -u http://localhost/signin -d passwords.txt -p '{ "username": "julien", "password": "FUZZ" }'

Pour réaliser une attaque de password spraying :
$ h4cktool -u http://localhost/signin -d users.txt -p '{ "username": "FUZZ", "password": "password" }'

L'objectif est de remplacer "FUZZ" par les mots du dictionnaire et d'envoyer le résultat dans le body d'une requête POST envoyée à l'URL

-u, --url
-d, --dict
-p, --post

 
https://www.python-httpx.org/
HTTPX
A next-generation HTTP client for Python.
Oppliger
 — 
Hier à 14:32

# Le chiffre de César

# notes :
# ord("a")
# chr("68")

cleartext = "bonjour"
ciphertext = ""

# pour chaque caractère
#    obtenez la valeur numérique du caractère
#    incrémentez cette valeur de 3
#    convertissez cette valeur en caractère
#    concatenez le caractère à la chaîne ciphertext

Samir
 — 
Hier à 15:17
Image
Oppliger
 — 
08:53

# Mettez à jour votre script pour qu'il fonctionne de manière entièrement asynchrone.

# La lecture des fichiers doit être effectuée de manière asynchrone
# grâce à 'aiofile'
# cf: https://pypi.org/project/aiofile/
# La requête doit être effectuée de manière asynchrone avec 'httpx'
# cf: https://www.python-httpx.org/async/

 
Oppliger
 — 
09:59

# Étant donné une liste de notes :
# 14, 15, 10, 12, 8, 16, 11, 14, 19
# Affichez un rapport sous la forme suivante :

# Nombre de notes = 9
# Note 1 = 14/20 (Très bien)

report.py
3 Ko
Oppliger
 — 
11:14
git init

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

git add report.py
git commit -m "initial commit"
Oppliger
 — 
12:27
Pour utiliser github comme dépot distant, il faut passer par trois étapes : 

    Configurer l'authentification par clé pour votre compte GitHub

 
voir : https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
GitHub Docs
Adding a new SSH key to your GitHub account - GitHub Docs
To configure your account on GitHub.com to use your new (or existing) SSH key, you'll also need to add the key to your account.
Image

    Configurer l'agent SSH pour utiliser votre clé automatiquement avec SSH

voir : https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows
GitHub Docs
Generating a new SSH key and adding it to the ssh-agent - GitHub Docs
After you've checked for existing SSH keys, you can generate a new SSH key to use for authentication, then add it to the ssh-agent.
Image

    Ajouter le serveur distant à votre projet git

git remote add origin git@github.com:0ppliger/note_report.git

Vous pouvez maintenant envoyer vos modifications au serveur distant

git push -u origin master

Oppliger
 — 
13:34
https://github.com/0ppliger/exercices_python
GitHub
GitHub - 0ppliger/exercices_python
Contribute to 0ppliger/exercices_python development by creating an account on GitHub.
GitHub - 0ppliger/exercices_python
﻿

## ███████████████ 
## LES EXPRESSIONS
## ███████████████ 

# -- 📕 Définition
# Une expression :
# est une instruction atomique évaluée par l'interpréteur.

# Il en existe plusieurs types comme :

# 👉 les expressions arithmétiques
1 + 1 

# 👉 les concaténations
"julien" + "oppliger"

# 👉 les expressions logiques
18 < 30
True and True

# 👉 les appels de fonction
print("Hello world !")

# 👉 les affectations de variable
a = 10

# 👉 et plein d'autres !
#   (déclaration de variable et de fonction, condition, boucle, etc.)

# -- 🤔 Remarque:
# Les expressions sont évaluées 
# les unes après les autres du plus 
# bas au plus haut dans la hierarchie.

# eg, :
print(pow(4 ,3 + pow(3 * 2, 4)))
print(pow(4 , 3 + pow(6, 4)))
print(pow(4 , 3 + 1296))
print(pow(4 , 1299))
print(11910465487876695589717869) # ..

## █████████████
## Les variables
## █████████████

# -- 📕 Définition
# La déclaration de variable :
# indique au système que la variable existe
a = "variable déclarée"

# -- 📕 Définition
# l' affectation de variable :
# indique au système que la variable contient cette valeur
a = "variable affectée"

# -- Remarque:
# En python la déclaration d'une variable 
# se fait au moment de l'affectation.

# La variable est déclarée lorsqu'elle est affectée pour la première fois.
b = "ma valeur" 
# Elle peut être réaffectée mais pas redéclarée.
b = "une autre valeur" 

## █████████ 
## LE TYPAGE
## █████████ 

# -- 📕 Définition
# Un type :
# détermine le type de valeur qu'une variable stock stock.

# Voici les principaux types de python:

# 👉 chaîne de caractères (str)
a = "une chaîne de caractères"
a = 'une chaîne de caractères'

# 👉 nombre entier (int)
entier = 10

# 👉 nombre flottant (float)
flottant = 10.0

# 👉 booléen (bool)
booleen = True
booleen = False

# -- 🤔 Remarque:
# Python est un langage a typage dynamique fort.
# Cela signifie qu'il ne va pas réaliser de conversion de type pour vous. Si une
# fonction attend une chaîne vous devez lui passer une chaîne.

# eg,
# age stock un entier (int)
age = 20 
# une concaténation attend des chaînes (str)
print("julien" + str(age))
# str(age) permet de convertir un type int en type str.

# -- 🤔 Remarque:
# Python est un langage à typage dynamique.
# Cela signigie qu'une même variable peut recevoir différents types.

# eg,
a = 10
a = "une chaîne"

## ██████████████████████████
## Les structures de contrôle
## ██████████████████████████ 

# -- 📕 Définition
# une structure de contrôle :
# permet de modifier le flux d'exécution d'un programme.

# On y trouve notamment :

# 👉 Les conditions

if age > 18:
    print("accès autorisé")
else:
    print("accès interdit")

# 👉 Les boucles

for nombre in range(0, 10):
    print("nombre = " + str(nombre))

## ██████████████
## Les conditions
## ██████████████

# Les expressions logiques

if age > 18:  # supérieur
    pass
if age >= 18: # supérieur ou égal
    pass
if age < 18:  # inférieur
    pass
if age <= 18: # inférieur ou égal
    pass
if age == 18: # égal
    pass
if age != 18: # différent
    pass

# L'opérateur "and"

if age >= 18 and age <= 25:
    print("Appliquer le tarif jeune")

#  ┌─────┬─────┬─────┐
#  │  A  │  B  │ A∧B │
#  ├─────┼─────┼─────┤
#  │  0  │  0  │  0  │
#  │  0  │  1  │  0  │
#  │  1  │  0  │  0  │
#  │  1  │  1  │  1  │
#  └─────┴─────┴─────┘

# L'opérateur "or"

if age == 18 or age == 80:
    print("bravo")

#    ┌─────┬─────┬─────┐
#    │  A  │  B  │ A∨B │
#    ├─────┼─────┼─────┤
#    │  0  │  0  │  0  │
#    │  0  │  1  │  1  │
#    │  1  │  0  │  1  │
#    │  1  │  1  │  1  │
#    └─────┴─────┴─────┘

## ██████████
## Les listes
## ██████████

# -- 📕 Définition
# une liste :
# permet de stocker un ensemble ordonné de valeurs.

les_notes_de_la_classe = [12, 16, 8, 14]
# indices :               0   1   2  3

# -- 🤔 Remarque:
# On peut accéder aux éléments d'une liste grâce à leur indice.
# L'indice commence toujours à 0 et termine toujours à la taille du tableau - 1.

## ███████████
## Les boucles
## ███████████

# -- 📕 Définition
# une boucle :
# permet de répéter un bloc d'instructions

# La syntaxe est :
# for ELEMENT in LIST:
#     instructions

for note in les_notes_de_la_classe:
    print(note)

## -- 🤔 Remarque:
# Pour répéter une opération 10 fois, vous pouvez 
# générer une liste de [0 à 10] (10 exclu) 
# grâce à la fonction "range"

for index in range(0, 10):
    print("Rentrez vous ça dans la tête")

