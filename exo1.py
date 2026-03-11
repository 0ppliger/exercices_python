# Déclarez une liste de note, transformez les notes sur 20 en note sur 100 et affichez les sous la forme
# note sur 100 = 50
# etc.
# Voici les notes à utiliser :
# 10 14 12 8 7 20

notes = [10, 14, 12, 8, 7, 20]

for note in notes:
    note_100 = note * 5
    print("note sur 100 = " + str(note_100))