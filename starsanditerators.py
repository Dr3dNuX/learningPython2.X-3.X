D = dict(a='Bob', b='dev', c=40.5)

def printdict(a,b,c):
    print(a)
    print(b)
    print(c)

printdict(**D)

s = 'spam'
s[1:] + s[:1]
print()

#for i in range(len(s)):
#    s = s[1:] + s[:1]
#    print(s, end=' ')