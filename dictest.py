table = {'1975': 'Holy Grail',
'1979': 'Life of Brian',
'1933': 'Life of Brian',
'1983': 'The Meaning of Life'}

serach = "Life of Brian"

for key in table:
    item = table['{}'.format(key)]
    if item == serach:
        print("This is the key for your item {}".format(key))