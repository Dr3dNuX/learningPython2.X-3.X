person = {'name': 'Jen', 'age': 22}
person_list = ['Jen', 22]
float_number = 2.3453234342

# string formatting using str concat
sentence = 'My name is ' + person['name'] + ' And i am ' + str(person['age']) + ' years old'

# string formatting using format string method
sentence = 'My name is {} and i am {} years old'.format("Jen", 22)

# string formatting using keys and values from a dic
sentence = 'My name is {} and i am {} years old'.format(person['name'], person['age'])

# same thing but using index locations otherwise it will place the values into the place holders using relitive postion.
# as you can see i swaped the varables in the format call
sentence = 'My name is {1} and i am {0} years old'.format(person['age'], person['name'])

#passing a list to the method and acessing the list items by index {0[2]}
sentence = 'My name is {0[0]} and i am {0[1]} years old'.format(person_list)

# things can be repeated if you use the same index number in the format placeholder
sentence = 'My name is {0} and my frends name is also {0} i just turned {1}'.format(person['name'],person['age'])

# using keys in the place holders and passing the dictionary
sentence = 'My name is {0[name]} and i am {0[age]} years old'.format(person)

# placeholder key values
sentence = 'My name is {name} and i am {age} years old'.format(name='Jen', age=22)

# unpacking a dictionay 
sentence = 'My name is {name} and i am {age} years old'.format(**person)

# flating point formatting and deciaml point truncation
number_formatting = 'formatting a floating point number and reducing its decimal points to 3{:.3f}'.format(float_number)

print(number_formatting)

# adding zero padding to numbers in the format method
for i in (1,11):
    print('Number {:02}'.format(i))

# method only comma formatting
sentence = '1 megabyte in bytes = {:,} bytes'.format(1000 ** 2)

print(sentence)