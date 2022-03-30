my_list = [2, 4, 7, 1, 3, 8, 9, 4]
print('My list')
print(my_list)

# We access individual elements in a list the same way we do with individual
# characters in a string. Just like strings, the index starts with 0.
print('Value at index 0 is %s' % my_list[0])
print('Value at index 4 is %s' % my_list[4])

# Also just like a string, we can use the len() function for the list length.
print()
print('Length of my list is %s' % len(my_list))

# You can use the range() function to populate a list.
num_list = list(range(7))
print()
print('List of numbers')
print(num_list)

# Slices work the same way with lists as they did with strings.

# includes the 4th and 5th values - the values at index 3 and 4
print()
print('Slice 3:5')
print(num_list[3:5])

# includes all of the values at index 3 until the end
print()
print('Slice 3:')
print(num_list[3:])

# includes the first 3 values in the list
print()
print('Slice :3')
print(num_list[:3])

# includes the last two values
print()
print('Slice -2:')
print(num_list[-2:])

# includes all but the last two values
print()
print('Slice :-2')
print(num_list[:-2])

