# Converting and checking numeric input.

some_input = input('Enter a number.')

# note - input will give us a string, and we need to convert that to an int.
num = int(some_input)

if num == 0:
    print("That number is definitely 0.")

