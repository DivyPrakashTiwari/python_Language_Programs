# Ask the user to input the number of elements they want in the list
n = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the elements
l = []

# Initialize a variable to store the sum of the elements
s = 0

# Print a message to prompt the user to enter the elements of the list
print("Enter the elements of the list:")

# Use a for loop to iterate through the range of the number of elements
for i in range(n):
    # Ask the user to input an element and convert it to an integer
    a = int(input())
    # Append the element to the list
    l.append(a)

# Use a for loop to iterate through the list
for i in range(n):
    # Add the current element to the sum
    s = s + l[i]

# Print the sum of the elements of the list
print("The sum of the elements of the list is:", s)