prompt = 'Enter a number, or enter "stop" to end.'
user_input = ''

while user_input != 'stop':
    user_input = input(prompt)
    if user_input == 'stop':
        break
    
    num = float(user_input)
    double_num = num * 2

    print('Double %s is %s.' % (num, double_num))

