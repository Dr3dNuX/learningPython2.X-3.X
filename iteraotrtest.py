Z = zip((1, 2, 3), (10, 11, 12))
L = [1, 2 ,3 ,4]
#print(dir(Z))
#print(dir(L))
i1 = iter(L)
i2 = iter(L)

b1 = iter(Z)
b2 = iter(Z)

print(str(next(i1)) + "i1")
print(str(next(i1)) + "i1")
print(str(next(i1)) + "i1")
print(str(next(i2)) + "i2")

print(str(next(b1)) + "b1")
print(str(next(b1)) + "b1")
print(str(next(b2)) + "b2")

print(i1 is i2)
print(b1 is b2)