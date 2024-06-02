# Ask the user for the number of elements they want in the list
n = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the elements
l = []

# Print a message to prompt the user to enter the elements
print("Enter the elements of the list one by one:")

# Use a for loop to iterate through the range of the number of elements
for i in range(n):
    # Ask the user for the element and convert it to an integer
    a = int(input())
    # Append the element to the list
    l.append(a)

# Print the elements of the list
print("The elements of the list are:")
# Use a for loop to iterate through the range of the number of elements
for i in range(n):
    # Print the element and add a space after it
    print(l[i], end=" ")
    # Increment the value of i by 1
    i = i + 1