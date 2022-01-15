

def filt(x):
    if x < 0:
        return x
    else:
        return False



ran = list(range(-5, 5))

print(list(filter(filt, ran)))

