

def ListSqu(x):
    for number in x:
        if x == "stop":
            print('stopping')
        else:
            x = yield number ** 2

d = ListSqu([1,2,3,4])

for i in d:
    if i > 4:
        d.send('stop')
        break
    else:
        print(i)

print("nice")

def thingbing():
    yield from [1,2,3,4]
    yield from 'String'
    yield from {1,2,3,4}

print(next(thingbing()))