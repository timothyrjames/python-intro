value = input('What is your age?')
age = int(value)

if age < 21:
    print('In the United States, you can\'t by alcohol.')
    if age < 16:
        print('In the United States, you can\'t drive a car.')
    else:
        print('You can drive a car in the United States.')
else:
    if age > 65:
        print('Congratulations! You can get senior discounts!')
    else:
        if age > 23:
            print('You were born in the last century.')


