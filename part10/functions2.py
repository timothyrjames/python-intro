def say_hello():
    print('Hello!')

def sum(a, b):
    return a + b


say_hello()

s = sum(5, 8)
print(s)

# Note one of the interesting capabilities in Python - because the + operator
# works as concatenation and addition, we can use the sum function on both str
# types and int types (as well as float types).

sentence = sum('this is ', 'a sentence')
print(sentence)

# Note that you can also name parameters when you call a function; this allows
# additional flexibility in parameter ordering.

s = sum(b='This', a='That')
print(s)

