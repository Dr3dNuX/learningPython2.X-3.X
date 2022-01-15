print("please enter a string to be converted to ASCII binary")

string = input(">> ")
binstring = []
cleanbinstring = []
binarysting = ""


for c in string:
    binstring.append(str(bin(ord(c))))

for s in binstring:
    cleanbinstring.append(s[2:])

for b in cleanbinstring:
    binarysting += "{} ".format(b)

print(binarysting)