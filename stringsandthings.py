
# escape chars
print("Hello\t, \nWorld!!")

# raw strings to surpress escaping
# ps you can use / on windows file names
# you dont need a raw string because the file object is cross platform
print(r"C:\windows\users\nathen")

# basic string operations concat repit and builtin functions
print(len("Hello, World!!"),"Hello, " + "World!!", "goodbye" * 3 )


# steping though a string because strings are itarable
string = "Hello World!!"

for c in string:
    print(c)

# basic Membership test operations
print("Hello" in "Hello, World!!")
print("Hazbin" not in "Hello, World!!")
print("Hello, World!!" == "Hello, World!!")

# indexing and slicing strings
# string = "Hello, World!!"

#slice starting at index one to index 2
print(string[1:2])
# negitive index slicing starting from the back of the index
print(string[:-2])
# slicing using a stepping operation from the start every seconed char till'
# The end of the string
print(string[:len(string):2])

# string converting tools

string = "22"
number = 35

# convert an int or float to a string object
print(string + str(number))

# convert a string to and int or float object
print(int(string) + number)

# grabbing letters using item index in string litteral
string = "Hello, World!!"
print(string[8])