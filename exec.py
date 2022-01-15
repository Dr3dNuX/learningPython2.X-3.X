

while True:
    user_input = input('>> ')
    try:
        exec(user_input)
    except:
        print('error try again... ')