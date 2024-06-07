# Get the input string from the user
s = input("enter the string")

# Calculate the length of the input string
l = len(s)

# Print a message to indicate what the following output will be
print("ASCII value of characters are")

# Iterate over each character in the input string
for i in range(0, l):
    # Print the character and its corresponding ASCII value
    print(s[i], "=", ord(s[i]))