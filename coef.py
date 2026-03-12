# Implémentez un script "coef.py" qui s'utilise comme suit:
# coef.py 14:2 16:2 7:1 12:4
# Afficher la moyenne pondérée de cette liste de notes sur 20

# L'objectif est de gérer toutes les erreurs possibles.
# Soit avec des préconditions, soit avec try..except
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions

# NB: utilisez str.split(separator) pour séprarer la note du coef
# https://docs.python.org/3/library/stdtypes.html#str.split

import sys

sys.argv.pop(0)

if len(sys.argv) < 1:
    print("error: not enough arguments")
    exit(1)

notes = []
for arg in sys.argv:
    splitted = arg.split(":")
    
    if len(splitted) != 2:
        print(f"error: {arg} is note a well formatted note")
        exit(1)        

    try:
        note = {
            "value": float(splitted[0]),
            "coef": float(splitted[1])
        }
    except ValueError:
        print(f"error: {arg} must be made of numbers")
        exit(1)

    if note["value"] < 0 or note["value"] > 20:
        print(f"error: note {note['value']} out of range")
        exit(1)

    if note["coef"] < 0:
        print(f"error: coef {note['coef']} out of range")
        exit(1)
        
    notes.append(note)
        

total = {
    "value": 0,
    "coef": 0
}
for note in notes:
    total["value"] = total["value"] + note["value"] * note["coef"]
    total["coef"] = total["coef"] + note["coef"]

avg = total["value"] / total["coef"]
print(avg)
