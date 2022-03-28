prompt = 'Enter a number, or enter "stop" to end.'
user_input = input(prompt)

while user_input != 'stop':
    num = float(user_input)
    double_num = num * 2

    # If we want to insert 2 values into a string, we use %s two times, 
    # and enclose the 2 values in parentheses, like what you see below.
    print('Double %s is %s.' % (num, double_num))

    # This last statement is important. Next, we'll discuss why.
    user_input = input(prompt)

