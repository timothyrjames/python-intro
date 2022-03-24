num1 = int(input('Enter one number.'))
num2 = int(input('Enter another number.'))
num3 = int(input('Enter one more number.'))

if num1 >= num2 and num1 >= num3:
    print('%s is the greatest of those three numbers.' % num1)
elif num2 >= num3 and num2 >= num1:
    print('%s is the greatest of those three numbers.' % num2)
elif num3 >= num2 and num3 >= num1:
    print('%s is the greatest of those three numbers.' % num3)

