from os import sched_get_priority_max


s = 'spam'

e = enumerate(s)

print(e.__next__())
print(e.__next__())
print(e.__next__())