# Store input numbers

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Add two numbers
print('The sum of {0} and {1} is {2}'.format(num1,num2,sum))


#Alternative to this, we can perform this addition in a single statement without using any variables as follows
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))
