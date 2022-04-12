import random

finished = False

while not finished:
    number = random.randint(0, 100) + 1
    guess = -1

    while guess != number:
        user_input = input('Guess a number from 1 to 100. [Enter] to quit.')
        if user_input:
            guess = int(user_input)
            if guess == number:
                print('You got it!')
            elif guess < number:
                print('Your guess is too low.')
            elif guess > number:
                print('Your guess is too high.')
        else:
            finished = True
            print('The number was %s.' % number)
            break

