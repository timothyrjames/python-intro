# Nesting if statements to show multiple conditions.

some_input = input('Enter a number.')
num = int(some_input)

if num > 1000:
    print('That\'s a really big number!.')
    if num > 10000:
        # this line is indented 8 spaces.
        print('That\'s a really really big number!')

    # To continue this level of execution, just remove the indent.
    print('This is part of the first if statement; if num > 1000.')

