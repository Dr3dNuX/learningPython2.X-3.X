import time


timerinput = int(input('enter time> '))
timez = 0
for s in range(timerinput):
    time.sleep(60)
    timez += 1
    print(timez)

print('timer done :)')

import os
for (root, subs, files) in os.walk('.'):
    for name in files:
        if name.startswith('call'):
            print(root, name)