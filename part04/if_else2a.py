# This example extends if_else2.py to illustrate when to use "or"

food = input('Guess my favorite food.')

if food == 'pizza' or food == 'tacos':
    # Because we're using the same output for either case, we can use "or"
    print("That is correct.")
else:
    print("That's not it.')

