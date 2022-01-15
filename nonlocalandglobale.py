def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: print('This is x {} This is i {}'.format(x, i)))
    i = 88
    return acts

acts = makeActions()

print(acts[0])

acts[0]('hello')
acts[1]('bello')
acts[2]('cello')
acts[3]('gello')
acts[4]('pello')

s = 