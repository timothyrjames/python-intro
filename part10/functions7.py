def is_prime(num):
    isp = True
    for v in range(num - 1, 1, -1):
        if num % v == 0:
            isp = False
            break

    return isp

print(is_prime(7))
print(is_prime(91))
print(is_prime(80))
print(is_prime(1223231))

