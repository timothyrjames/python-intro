num1 = int(input('Enter one number.'))
num2 = int(input('Enter another number.'))
num3 = int(input('Enter one more number.'))

greatest = num1

if num2 >= num3 and num2 >= num1:
    greatest = num2
elif num3 >= num2 and num3 >= num1:
    greatest = num3

print('%s is the greatest of those three numbers.' % greatest)

