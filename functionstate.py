import gc


def makeCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        print('The count is {}'.format(count))
    return counter

f1 = makeCounter()
f1()
f1()
f1()