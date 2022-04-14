import math

def get_factors(number):
    # First we create an empty set to store the factors.
    result = set()

    # To find all the factors, we need to iterate up to the square root.
    root = math.sqrt(number)

    # range() requires the second parameter to be an int.
    root = int(root)

    # If the number is square, we need to iterate including the square root.
    for i in range(2, root + 1):
        if number % i == 0:
            # When we find a factor, we add that factor and its other side.
            result.add(i)
            result.add(number // i)
    return result

for i in range(200, 250):
    factors = get_factors(i)
    if factors:
        print('The factors of %s are %s.' % (i, factors))
    else:
        print('%s is prime.' % i)

