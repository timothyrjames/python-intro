user_input = ''

while user_input != 'quit':
    user_input = input("Enter a number but don't enter 5! Enter 'quit' to end.")
    if user_input == 'quit':
        break
    num = int(user_input)
    if num == 5:
        print('5 is no good!')
        continue
    print('Thank you! Your number is %s.' % num)


