#Write a program that takes two numbers and prints:
#Their sum, difference, and product
#Whether the first number is greater than the second
int1=int(input('Enter first number'))
int2=int(input('Enter second number'))
int3=int1+int2
int5=int1*int2
print('The product is',int5)
print('The sum is',int3)
int4=int1-int2
print('The difference is',int4)
if int1>int2:
    print('The first number is greater than the second')
elif int1==int2:
    print('The first number is equal to the second')
else:
    print('The first number is not greater than the second')
print(int1>int2 or int1==int2)
