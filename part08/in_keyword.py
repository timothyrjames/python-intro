animals = ['aardvark', 'buffalo', 'cat', 'dog']
# We can use the "in" keyword to determine if something is in our structure.
print('Is cat in our list?')
print('cat' in animals)

states = {
    "PA": "Pennsylvania",
    "NY": "New York",
    "NJ": "New Jersey",
    "IA": "Iowa",
}
print()
print('Is NJ a key in our dictionary?')
print('NJ' in states)
print('Is MO a key in our dictionary?')
print('MO' in states)

ids = set()
ids.add('124312')
ids.add('124323')
ids.add('124329')
ids.add('124317')
ids.add('124321')

print()
# Do we have this ID? 
id = '124322'
print('Does %s exist in the set?' % id)
print(id in ids)

# Do we have this ID? 
id = '124312'
print('Does %s exist in the set?' % id)
print(id in ids)

