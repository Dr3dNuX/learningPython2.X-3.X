def thingbing():
    yield from [1,2,3,4]
    yield from 'String'
    yield from {1,2,3,4}


for c in thingbing():
    print(c)