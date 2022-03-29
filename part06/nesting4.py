for i in range(2, 100):
    is_prime = True
    for v in range(i - 1, 1, -1):
        if i % v == 0:
            is_prime = False
            # Since we only need ONE evenly divisible number (v) for our 
            # number (i) to be prime, we can break.
            # Note that this only breaks us out of the **inner** loop.
            break

    if is_prime:
        print(i)

