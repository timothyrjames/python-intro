my_string = '98765'

print("Let's subtract 1 from each of %s." % my_string)
for c in my_string:
    num_value = int(c)
    print(num_value - 1)
else:
    print("That's all!")

