
from typing import Iterator, Sequence


def scramble(seq: Sequence)-> list:
    """
    Scramble function
    This fucntion returns a scrambled list
    of any seqence data type passed in
    example call/ scramble('spam') -> 
    ['spam', 'pams', 'amsp', 'mspa']
    """

    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

scramble('spam')

def scramble_iter(seq: Sequence) -> Iterator:
    """
    Scrable Generator
    This Generator fucntion will return
    an iter of a scambled sequence
    """
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq
    
b = scramble_iter([1,2,3])
print(next(b))
print(next(b))
print(next(b))