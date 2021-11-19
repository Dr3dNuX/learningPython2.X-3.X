string = "Hello, World!"

MultiLineString = """
Hello,
World!!
"""

print('The original string -> {}'.format(string))

print('The find method returns the index of the substring you enter -> {}'.format(string.find('l')))

print('The upper method will return the string in all uppercase -> {}'.format(string.upper()))

print('The lower method will return the sting in all lowercase -> {}'.format(string.lower()))

print('The split method will split the string into substrings using a dilimter of your chosing then return a list object -> {}'.format(string.split(',')))

print('The find method will find a substring and return the index of the first letter of substring -> {}'.format(string.find('ell')))

print('The isalpha method will return a bool if the litteral only contains alphabet letters -> {}'.format(string.isalpha()))

# There are meny more methods but this demos some of them 