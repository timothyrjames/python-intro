user_input = input("Enter a number and I'll tell you some of its multiples.")

# This looks like it might never end, but we use break to end the loop below.
while True:
    value = int(user_input)
    
    i = 1
    while i <= 5:
        print('%s is a multiple of %s.' % (value * i, value))
        i += 1
    
    user_input = input('Enter another number, or enter "end" to quit.')
    if user_input == 'end':
        break

