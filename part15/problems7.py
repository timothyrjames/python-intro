word_counts = {}

finished = False

while not finished:
    text = 'Enter a sentence and I\'ll count your words! Enter a blank to end.'
    user_input = input(text)
    if user_input:
        user_input = user_input.lower()
        words = user_input.split(' ')
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    else:
        finished = True

print('Here are the results:')
for word in word_counts:
    print('%s: %s' % (word, word_counts[word]))

