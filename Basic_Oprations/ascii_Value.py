# This line prompts the user to enter any character and stores it in the variable 'c'
c = input("Enter any character")

# The ord() function is used to convert the character 'c' to its corresponding ASCII value
# and then prints the string "The ASCII value of <character> is: <ASCII value>"
print("The ASCII value of " + c + " is: ", ord(c))