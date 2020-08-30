#Python Program to Swap Two Variables

#Source Code: Using a temporary variable

# Python program to swap two variables

#x = 5
#y = 10


# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values

tmp = x
x = y
y = tmp


print("x = " ,x)
print("y = " ,y)

#Source Code: Without Using Temporary Variable

#above but without the use of any temporary variable.

x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)


#Addition and Subtraction


x = x + y
y = x - y
x = x - y

x, y = y, x
print("x =", x)
print("y =", y)
#Multiplication and Division


x = x * y
y = x / y
x = x / y

x, y = y, x
print("x =", x)
print("y =", y)
#XOR swap

#This algorithm works for integers only

a = 34
b = 45

a = a ^ b
b = a ^ b
a = a ^ b

print('The value of a after swapping : {}'.format(a))
print('The value of b after swapping : {}'.format(b))

