import sys
FILE = open('out.txt','a')
# this program will showcase all the cool stuff you can do with the print fucntion / statment in 2.X


# in python 3.X this print feture is a fuction

print("Hello World")
# it opens a connection to the sys.stdout file and writes a stream of bytes to that file as well as converts the data type to its
# texual format using the str() built-in 

# you can change the file print writes to using the print("object", file='filename.txt') keyword argument.

print("Hello, World!!", file=FILE)

# there are more keyword auguemnts in the print function

# like the sep='separator' keyword it adds or removes the separator
#between objects
print("Hello","World",sep='$$$')

# what the statemtns ends with default is \n
print("Hello","World", end='$$$')

# changeing the print stream by changing the stdout file pointer
sys.stdout = FILE

print("Hello World and Welcome to the Stream")