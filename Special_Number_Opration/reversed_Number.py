# This code snippet is designed to reverse the digits of a given integer input

n = int(input("Enter the number to be reversed: "))  # Prompt user for input and convert it to integer

while(n!= 0):  # Continue looping until the input number becomes 0 (i.e., all digits have been processed)
    r = n % 10  # Obtain the remainder of the division of the number by 10, which is the last digit
    print(r, end="")  # Print the last digit without a newline character
    n = n // 10  # Remove the last digit by integer dividing the number by 10