states = {
    "PA": "Pennsylvania",
    "IA": "Iowa",
}

keys = states.keys()
print('Keys, before a dictionary change:')
print(keys)

# keys will change based on changes to the dictionary.
states['VT'] = 'Vermont'
print('Keys, after a dictionary change:')
print(keys)

v = states.values()
print('Values, before another change:')
print(v)

# values will also change based on changes to the dictionary.
states['CO'] = 'Colorado'
print('Values, after another change:')
print(v)

# We can copy a dictionary.
states_copy = states.copy()

# We can remove a value from the dictionary.
states.pop('IA')

print('Dictionary after removing "IA":')
print(states)

# We can remove everything from the dictionary.
states.clear()

print('Our dictionary, after clearing it:')
print(states)

print('Our copy, after clearing the original:')
print(states_copy)

