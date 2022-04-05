def sum(*values):
    result = 0
    for v in values:
        result += v
    return result

print(sum(3, 2, 4, 3, 1, 3, 3, 5, 8, 9))
print(sum())
print(sum(10, 20))

