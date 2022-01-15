

def intersect(*t):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
            else:
                res.append(x)
    return res

l1 = [1,2,3,4]
l2 = [1,3,5,6]


print(intersect(l1,l2))
