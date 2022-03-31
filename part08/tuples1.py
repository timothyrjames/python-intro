# Tuples are declared with parentheses instead of square brackets.
not_a_list = (1, 2, 3, 4)

print('My tuple:')
print(not_a_list)

print('One element in my tuple:')
print(not_a_list[2])

print('Iterating over values in a tuple:')
for value in not_a_list:
    print('The square of %s:' % value)
    print(value * value)

# We can't set the value in a tuple. We'll get an error.
# The following line is commented so the code still works.
# not_a_list[2] = 7

# We *can* convert a tuple to a list.
became_a_list = list(not_a_list)

print('This is a list that used to be a tuple:')
print(became_a_list)

# We can change a value in the resulting list.
became_a_list[2] = 7

print('The list: ')
print(became_a_list)
print('The tuple: ')
print(not_a_list)

