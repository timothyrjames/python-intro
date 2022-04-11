import datetime

print('Right now:')
print(datetime.datetime.now())
print()

thanksgiving_2020 = datetime.datetime(year=2020, month=11, day=26)
print('Thanksgiving 2020:')
print(thanksgiving_2020)
print()

# We can also calculate differences in times.
march_31 = datetime.datetime(year=2022, month=3, day=31)
today = datetime.datetime.now()
print('The time between now and March 31:')
print(today - march_31)

delta = datetime.timedelta(days=180)
print('180 days ago was %s' % (today - delta))

