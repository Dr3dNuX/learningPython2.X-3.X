

while True:
    user_input = input('>> ')
    if user_input == 'stop':
        break
    elif not user_input.isdigit():
        print('Bad input...')
    else:
        print(int(user_input) ** 2)

print('goodbye...')


string = 'hello'
try:
    num = int(string)
except:
    print('>> type error try again..')