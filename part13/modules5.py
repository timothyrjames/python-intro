import random

print('Five random numbers:')
for i in range(5):
    print(random.random())
print()

print('Five random int values from 5 to 15:')
for i in range(5):
    print(random.randint(5, 15))
print()

print('A random uniform distribution of numbers:')
uniform_random_list = []
for i in range(12):
    random_uniform_num = random.uniform(0, 10)
    uniform_random_list.append(round(random_uniform_num, 2))
print(uniform_random_list)

