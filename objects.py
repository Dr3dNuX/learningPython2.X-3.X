class thing:
    pass

thing.name = 'bobadfasfdasdff asd'

i1 = thing()
i2 = thing()
i1.name = 'bainasdfasdfasdfaf asdfa'
thing.name = 'jain asdfasdf as df'
print(hex(id(i1.name)),hex(id(i2.name)),hex(id(thing.name)),)
print(i1.name, i2.name, thing.name)