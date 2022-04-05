def get_greeting(**person):
    greeting = 'Hello'
    if 'firstname' in person:
        greeting = 'Hello, ' + person['firstname']
    if 'middlename' in person:
        greeting = greeting + ' ' + person['middlename']
    if 'lastname' in person:
        greeting = greeting + ' ' + person['lastname']
    greeting = greeting + '!'

    return greeting


print(get_greeting(firstname='Sam'))
print(get_greeting(lastname='Smith', firstname='Sam'))
print(get_greeting(lastname='Smith', firstname='Sam', middlename='S'))

