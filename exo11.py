noms = ["bob", "alice", "carole", "daniel", "edgar"]

# expected = ["BOB", "ECILA", "ELORAC", "LEINAD", "RAGDE"]

def dothething(names: list) -> list:
    newlist = []
    for name in names:
        newlist.append(name[::-1].upper())

    # return [ name[::-1].upper() for name in names ]
    return newlist

print(dothething(noms))