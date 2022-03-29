# This will print out all of the prime numbers between 10 and 49.
for i in range(49):
    if i < 10 or i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        continue
    print(i)

