# This code snippet generates the Fibonacci series up to a given number 'n'

n = int(input("Enter the number: "))  # Prompt user to input a number

print("The Fibonacci series is: ")  # Inform user that the Fibonacci series will be printed

a = 0  # Initialize the first number in the Fibonacci series
b = 1  # Initialize the second number in the Fibonacci series
s = 1  # Initialize the sum of the current and previous numbers in the series

print(a)  # Print the first number in the series
print(b)  # Print the second number in the series

# Iterate through the range from 0 to n (inclusive)
for i in range(0, n + 1):
    s = s + i  # Calculate the sum of the current and previous numbers in the series
    print(s)  # Print the sum, which is the next number in the Fibonacci series