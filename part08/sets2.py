# The .add() method allows us to add values to the set.
ids = set()
ids.add('124312')
ids.add('124317')
ids.add('124323')
ids.add('124329')
ids.add('124317')
ids.add('124321')

print('A set of IDs:')
print(ids)

# We can remove a value from the set.
ids.remove('124317')
print('The set with one value removed.')
print(ids)

# How many unique items are in this list?
print('The size of the set:')
print(len(ids))

# Clearing all the items from a set.
ids.clear()
print('We cleared the set:')
print(ids)

