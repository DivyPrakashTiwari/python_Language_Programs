# This script checks if a given year is a leap year or not

n = int(input("Enter the year to be checked: "))  # Prompt user to input a year as an integer

# A leap year is divisible by 4, but not by 100, unless it is also divisible by 400
if (n % 4 == 0 and n % 100!= 0) or n % 400 == 0:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")