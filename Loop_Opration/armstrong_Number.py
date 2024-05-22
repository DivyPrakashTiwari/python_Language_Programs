# Take an integer input from the user
n = int(input("enter the number"))

# Initialize a variable '' to 0, which will store the sum of the cubes of each digit
s = 0

# Store the original value of 'n' in 'i', which will be used later for comparison
i = n

# Loop until 'n' becomes 0
while(n!= 0):
    # Calculate the remainder of 'n' when divided by 10, which gives the last digit
    r = n % 10
    
    # Calculate the cube of the last digit
    p = r * r * r
    
    # Add the cube of the last digit to ''
    s = s + p
    
    # Remove the last digit from 'n' by performing integer division by 10
    n = n // 10

# Check if the original number 'i' is equal to the sum of the cubes of its digits ''
if(i == s):
    # If they are equal, print that the number is an Armstrong number
    print(" yes the number is armstrong")
else:
    # If they are not equal, print that the number is not an Armstrong number
    print(" no the number is armstrong")