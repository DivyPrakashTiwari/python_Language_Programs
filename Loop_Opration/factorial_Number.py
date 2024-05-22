# This script calculates the factorial of a given number using a for loop

n = int(input("Enter the number: "))  # Prompt user for input and convert it to an integer

fac = 1  # Initialize the factorial variable with a value of 1

# Iterate from 1 to n (inclusive) using a for loop
for i in range(1, n + 1):
    fac = fac * i  # Calculate the factorial by multiplying the current iteration value with the previous factorial value
    i = ++i  # Increment the loop variable by 1 (this line is redundant and can be removed)

print("The factorial is:", fac)  # Output the calculated factorial