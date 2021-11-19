import fractions
import decimal


number = 2 ** 4

string = "123"

library = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

tuple = ("hello", 1, 2)

list = ["hello", 1, 2]

boolen = True

none = None

fraction = fractions.Fraction(3, 3)

Decimal = decimal.Decimal('3.142')

floating = 2.7

file = open('data.txt', 'w')
file.write("Hello World!!")
file.close()

print(string[1:5] + " World" * 3)

#print(string.replace("Hello", "Bruh"))
#print(string.split('/'))
#print(string.upper())

print(string.isalpha())