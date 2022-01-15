import time, sys

timer = time.time

def power(x):
    return x ** 2

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (Total time, last resault)
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

print(bestof(10000, power, 5))

