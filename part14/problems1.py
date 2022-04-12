days_31 = ['jan', 'january', 1, 'mar', 'march', 3, 'may', 5, 'jul', 'july', 7,
           'aug', 'august', 8, 'oct', 'october', 10, 'dec', 'december', 12]

days_30 = ['apr', 'april', 4, 'jun', 'june', 6, 'sep', 'september', 9, 'nov',
           'november', 11]

days_28_29 = ['feb', 'february', 2]


def add_entries(d, keys_list, value):
    for key in keys_list:
        key = str(key)
        d[key] = value


days = {}
add_entries(days, days_31, '31 days')
add_entries(days, days_30, '30 days')
add_entries(days, days_28_29, '28 or 29 days')


def prompt_user():
    return input('Please enter a month, or press enter to end.')


i = prompt_user()
while i:
    i = i.lower()
    if i in days:
        print('There are %s in that month.' % days[i])
        if i == '3' or i == 'mar' or i == 'march':
            print('That is the current month.')
    else:
        print('That input was not valid.')
    i = prompt_user()

print('Thanks for playing!')

