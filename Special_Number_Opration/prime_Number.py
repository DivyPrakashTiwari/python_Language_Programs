# Ask the user to input a number and store it in variable 'n'
n = int(input("Enter the number: "))

# Initialize variables 'i', 'j', and 'k' with values 'n', 1, and 0 respectively
i = n
j = 1
k = 0

# Start a while loop that runs until 'j' is less than or equal to 'n'
while j <= n:
    # Calculate the remainder of 'n' divided by 'j' and store it in variable 'f'
    f = n % j
    
    # Check if 'f' is equal to 0
    if f == 0:
        # If 'f' is equal to 0, increment the value of 'k' by 1
        k = k + 1
    
    # Increment the value of 'j' by 1
    j = j + 1

# Check if the value of 'k' is greater than 2
if k > 2:
    # If the value of 'k' is greater than 2, print that the number is not a prime number
    print("The number", i, "is not a prime number")
else:
    # If the value of 'k' is not greater than 2, print that the number is a prime number
    print("The number", i, "is a prime number")