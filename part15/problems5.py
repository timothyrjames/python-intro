def is_palindrome(word):
    # We use integer division here to get the halfway point in the string.
    halfway_point = len(word) // 2

    for i in range(halfway_point):
        # The first half index is i, this part is easy.
        first_half_index = i
        # The second half index is -i - 1.
        # The first iteration will be -0 - 1 = -1; the second will be -2, etc.
        second_half_index = -i - 1
        if word[first_half_index] != word[second_half_index]:
            return False
    # If we've checked all of the characters, we know it is a palindrome.
    return True

print('Is it a palindrome?')
finished = False
while not finished:
    user_input = input('Enter a word, or just press enter to finish.')
    if user_input:
        if is_palindrome(user_input):
            print('"%s" is a palindrome!' % user_input)
        else:
            print('"%s" is not a palindrome.' % user_input)
    else:
        finished = True

