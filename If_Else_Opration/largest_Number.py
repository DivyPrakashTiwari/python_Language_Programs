# This script takes three numbers as input and determines the largest number among them

a = int(input("Enter the first number: "))  # Taking the first number as input and converting it to integer

b = int(input("Enter the second number: "))  # Taking the second number as input and converting it to integer

c = int(input("Enter the third number: "))  # Taking the third number as input and converting it to integer

# Comparing a and b, if a is greater than b, then comparing a and c
# If a is greater than c, then a is the largest number
if a > b:
    if a > c:
        print("The largest number is ", a)

# Comparing b and c, if b is greater than c, then b is the largest number
elif b > a:
    if b > c:
        print("The largest number is ", b)

# If neither a nor b is greater than c, then c is the largest number
else:
    print("The largest number is ", c)