i = 0

print('Here is a slow way to compute every even number between 2 and 30.')
while i <= 30:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

