

from typing import Iterable


def addTen(x: Iterable):
    for number in x:
        yield number + 10

print(list(addTen([1,2,3,4,5])))