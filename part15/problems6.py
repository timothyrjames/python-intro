def is_anagram(word, word_to_check):
    # We create a dictionary to count all the letters.
    letters = {}
    for letter in word:
        # For every letter, we keep count.
        if letter not in letters:
            # The first time we see the letter, we set the value to 1.
            letters[letter] = 1
        else:
            # Every other time we see the letter, we add 1 to the value.
            letters[letter] += 1

    # Now, for the word we're checking, we remove the letters one by one.
    for letter in word_to_check:
        if letter not in letters:
            # If the letter is not there, it's not an anagram. We can return.
            return False
        else:
            # If the letter is there, we reduce the count by 1.
            letters[letter] -= 1
            if letters[letter] == 0:
                # If the count is 0, we remove it from the dictionary.
                letters.pop(letter)
    # If we haven't removed everything from letters, then it's not an anagram.
    if letters:
        return False
    # If we make it this far, every letter from the first word is in the 2nd.
    return True

print(is_anagram('angel', 'glean'))
print(is_anagram('sadder', 'dreads'))
print(is_anagram('night', 'thing'))
print(is_anagram('this is', 'not an anagram'))

