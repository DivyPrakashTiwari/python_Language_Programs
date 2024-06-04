n = int(input("Enter the number to be reversed"))  # Get the number from the user to be reversed
s = 0  # Initialize a variable to store the reversed number (not used in this code snippet)
print("the reverse of the number is")  # Print a message to indicate the output
while(n != 0):  # Loop until the number becomes 0
    r = n % 10  # Get the last digit of the number
    print(r, end="")  # Print the last digit without a newline
    n = n // 10  # Remove the last digit from the number