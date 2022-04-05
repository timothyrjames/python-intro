def sum(a, b, c=0):
    return a + b + c

def say_hello(name=''):
    if name:
        # If len(name) > 0, we get here.
        print('Hello, %s!' % name)
    else:
        # If len(name) == 0 or name is not defined, we get here.
        print('Hello!')


# Now we can call these functions with different numbers of parameters. 

s = sum(1, 3, 7)
print(s)

s = sum(9, 10)
print(s)

say_hello()
say_hello('Jerry')

# Note: now that we're using a default parameter, we can't use the "sum"
# function for strings anymore. Try uncommenting the line below to see.
# sum('a', 'b') # this will cause an error because of incompatible types.


# We can create as many of these parameters as we like, based on our needs.

def sum(a=0, b=0, c=0, d=0):
    return a + b + c + d

print(sum(3))
print(sum(3, 5))
print(sum(3, 5, 2))
print(sum(3, 5, 2, 4))

