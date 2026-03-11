# liste de note
# vous me calculez la moyenne

notes = [12, 14, 15, 16, 11, 10]

somme = 0
for note in notes:
    somme = somme + note

nombre = 0
for note in notes:
    nombre = nombre + 1

moyenne = somme / nombre

print(moyenne)