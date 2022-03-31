# We can declare a dictionary and populate it in one step. 
# This is a pretty common practice in Python.
states = {
    "PA": "Pennsylvania",
    "NY": "New York",
    "NJ": "New Jersey",
    "IA": "Iowa",
}
print('A populated dictionary:')
print(states)

# We can iterate over the keys in a dictionary.
print()
print('The values from a dictionary:')
for state_code in states:
    print(state_code + ": " + states[state_code])

