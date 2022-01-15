# oh boy theres a lot to code so lets get started.

l = [1, 2, 3, "Hello World"]
l2 =[4, 5, 6]

# list repetiton new list object
test = l * 3

print(type(test))

print("test if in place {}".format(l))

# new list object
print(l + l2)

# conveting a list to a string.
#keeps commas and [] braces though
string_list = str(l)
print(string_list[1:-1].replace(',',''))

# membership testing
print(3 in l)

# iteration
for x in l:
    print(x)

res = [c * 4 for c in 'SPAM']
print(res)