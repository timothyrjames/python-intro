values = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 10, 9, 8]
print(sorted(values))
print('The original is not sorted!')
print(values)

# This won't work:
# sorted(9, 8, 7, 6)

# This function also works on sets and dictionary keys.
duplicate_list = ['something', 'something', 'a thing', 'another thing']
my_set = set(duplicate_list)
print(sorted(my_set))

states = {
    "CA": "California",
    "NY": "New York",
    "NJ": "New Jersey",
    "IA": "Iowa",
    "PA": "Pennsylvania",
}
print(sorted(states))

