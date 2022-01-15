spam = 'spam'

a, b, c, d = 'spam' # sequence assiengments

[one, two] = ['Hello', 'World'] # list assignments
print(one, two)

three, four = 'goodbye', 'World' # using tuples to assignments

spam = ham = ram = 'lunch' # multitarget assignments

spam = 20
spam += 30 #augmented assignments shorthand and faster for spam = spam + 33
print(spam)

# more augmented assignments
spam *= 10
print(spam)
spam -= 10
print(spam)



'Hello,', 'World!!' # remeber this is a tuple


# exstened sequence unpacking
a, b, *c = 'Spam'
print(a, b, c)

*a, b, c = 'Spam'
print(a, b, c)

a, *b, c = 'Spam'
print(a, b, c)


# tuple assignment in use using loops

for a, b, c in (1,2,3), (4,5,6):
    print(a, b, c)


L = [1, 2, 3, 4]

while L:
    front, L = [0], L[1:]
    print(front, L)

s = {1, 2, 3, 4}

v, *b, c = s

print(v, b, c)

# += on lists is mapped to the .extend() method
L = [1, 2, 3 ,4]
L += [5, 6, 7]
L += 'spam'
print(L)

spam = 'Hello'

print(print(list(spam)))

