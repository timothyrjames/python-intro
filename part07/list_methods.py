num_list = list(range(5))
print('List of numbers from 0 to 4:')
print(num_list)

# .append() lets you add values to the end.
num_list.append(50)
num_list.append(60)

print('List of numbers after appending 50 and 60:')
print(num_list)

# .clear() is pretty straightforward.
num_list.clear()
print('After clearing:')
print(num_list)

# .index() will find a value.
stores_list = ['Walmart', 'Target', 'Costco', 'Big Lots']
print()
print('Using .index() to find Target:')
print(stores_list.index('Target'))

# A good way to think of .insert() is that you specify the index of the item you
# are inserting - everything else in the list moves to the right.
stores_list.insert(1, "Kohl's")
print('Inserted "Kohl\'s" at index 1:')
print(stores_list)

# .remove() removes an item, if it exists. Otherwise you get an error.
stores_list.remove('Target') # if you do this more than once, you'll get an error.
print('Removed "Target" from the list.')
print(stores_list)

# If you run this multiple times, the order will keep going back and forth.
stores_list.reverse()
print('Reversed the list.')
print(stores_list)

# .sort() will sort the list.
stores_list.sort()
print('Sorted the list.')
print(stores_list)

