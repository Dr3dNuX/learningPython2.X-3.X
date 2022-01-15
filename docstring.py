
s = 'spamIsGood'


def asum(x):
    sumOfLetters = 0
    for c in x:
        print('{} = ASCII({})'.format(c, ord(c)))
        sumOfLetters += ord(c)
    return sumOfLetters


print(asum(s))