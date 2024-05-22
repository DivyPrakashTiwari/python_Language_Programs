# Get the user input for the number of natural numbers to sum
n = int(input("enter the number"))

# Initialize a variable to store the sum of natural numbers
s = 0

# Iterate over the range of natural numbers from 1 to n (inclusive)
for i in range(1, n+1):
    # Add the current natural number to the sum
    s = s + i
    
    # Increment the counter (not necessary in this case, as the loop will handle it)
    i = i + 1

# Print the result: the sum of the natural numbers
print("the sum of the natural number is", s)