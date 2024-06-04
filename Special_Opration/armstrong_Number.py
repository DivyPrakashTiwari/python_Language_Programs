# Get the number to be checked from the user
n = int(input("Enter the number to be checked"))

# Initialize a variable to store the sum of the cubes of the digits
s = 0

# Store the original number in a separate variable
i = n

# Loop until the number becomes 0
while (n != 0):
    # Get the last digit of the number
    r = n % 10
    
    # Calculate the cube of the last digit
    p = r * r * r
    
    # Add the cube to the sum
    s = s + p
    
    # Remove the last digit from the number
    n = n // 10

# Check if the sum is equal to the original number
if (s == i):
    # If true, print that the number is an Armstrong number
    print("yes,", s, "is an Armstrong number")
else:
    # If false, print that the number is not an Armstrong number
    print("no,", i, "is not an Armstrong number")