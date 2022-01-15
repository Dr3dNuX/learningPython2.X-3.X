def capital_indexes(seq):
    dexOfCaps = []
    dex = 0
    for c in seq:
        if c.isupper():
            dexOfCaps.append(dex)
            dex += 1
        else:
            dex += 1
            continue
    return dexOfCaps


print(capital_indexes('HellOWorld'))