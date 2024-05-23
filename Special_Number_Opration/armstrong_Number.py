# This program checks if a given number is an Armstrong number
n = int(input("Enter the number: "))  # Get user input and store it in variable 'n'

s = 0  # Initialize variable 's' to 0, which will be used to store the sum of cubes of digits
i = n  # Store the original number in variable 'i' for later comparison

# Loop through the digits of the number
while n!= 0:
    r = n % 10  # Extract the last digit
    p = r * r * r  # Calculate the cube of the digit
    s = s + p  # Add the cube to the sum
    n = n // 10  # Remove the last digit from the number

# Check if the sum of cubes of digits is equal to the original number
if i == s:
    print("Yes, the number is Armstrong")
else:
    print("No, the number is not Armstrong")