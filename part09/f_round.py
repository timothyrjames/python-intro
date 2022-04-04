print(round(12.51))
print(round(12.512423, 2))
print(round(-1111.2752342, 1))
print(round(100))

# This probably won't matter much in practice, but note that rounding to 0
# decimal places will return an int, not a float.
value = 9.99999
rounded = round(value)
print(type(rounded))

