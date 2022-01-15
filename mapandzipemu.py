def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    
    return res

def myzip(*seq):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0), for s in seqs))

d = zip([1,2,3,4])
print(next(d))

print(mymap(abs, [1,-2,3,-4]))

def mymap2