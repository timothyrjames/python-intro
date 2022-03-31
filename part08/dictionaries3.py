states = {
    "PA": "Pennsylvania",
    "NY": "New York",
    "NJ": "New Jersey",
    "IA": "Iowa",
}

# Using .items(), we can iterate over the keys *AND* values.
print('Another way to show the values from a dictionary:')
for state_code, state in states.items():
    print(state_code + ": " + state)

