
import sys
from typing import Generator


list_comp = [x * x for x in range(10) if x % 2 == 0]
dict_comp = {x : y for x in [1,2,3] for y in ['a','b','c']}
set_comp = {x for x in range(10) if x%2 == 0}
gen_comp = (x for x in [1,2,3,4] if x%2 == 0)

fun = lambda x: (v for v in x if v > 5)

def genfunc(x: int)-> Generator:
    """
    returns a generator object that 
    yeilds interagers from a range
    for example genfunc(5)

    yields -> 1
    next()
    yields -> 2
    next()...
    yields -> 5

    """
    i = 0
    while i < x:
        i += 1
        yield i

def printthings(*objects, Pad= ' ', ):
    stdout = sys.stdout
    stdout.write(str(objects) + '\n')

printthings('Hello','World')

    
b = genfunc(7)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

c = 'c'.isupper