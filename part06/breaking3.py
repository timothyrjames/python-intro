# Let's see if we can find the x.

for letter in 'the quick brown fox jumps over the lazy dog':
    if letter == 'x':
        print('We found an x!')
        break
    else:
        print('%s is not an x.' % letter)

