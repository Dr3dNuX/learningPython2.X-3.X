x = False
y = True
a = 0
while a < 10:
    if x:
        print("Break Statment")
        break
    elif y:
        print("Continue Statment")
        a += 1
        #continue
    print("continue blocks me from running")
    print("it jumps to the top of the loop")
else:
    print('loop finished without hitting break statment')


while False:
    print('The loop was true')
else:
    print("The loop was false")
