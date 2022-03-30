# You can use list() to create an empty list, but this is not common in Python.
my_list = list()
print('An empty list:')
print(my_list)

# The more common way in Python is to assign a variable to an empty list.
my_list = []
print()
print('Another empty list:')
print(my_list)

# You can create a list from something else - but it has to be iterable.
# A string will work.
s = 'word'
character_list = list(s)
print()
print('A list of characters made from a string:')
print(character_list)

# You can also create a copy of a list from a list.
list_copy = list(my_list)
print()
print('A copy of a list:')
print(list_copy)

