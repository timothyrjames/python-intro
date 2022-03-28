num = 1

print("Let's count to a billion!")
while num < 1000000000:
    print(num)
    num += 1
    
    if num > 10:
        # This stops us from going too far.
        print('On second thought, a billion is too many.')
        break


