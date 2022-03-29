# First, we iterate from 2 to 100.
for i in range(2, 100):
    # Let's assume this value is prime.
    is_prime = True

    # We count backward from i - 1.
    for v in range(i - 1, 1, -1):
        # If the number is divisible by v, then we know it's not a prime number.
        if i % v == 0:
            is_prime = False

    # Output the value if it's prime.
    if is_prime:
        print(i)

