# Get the size of the list from the user
n = int(input("Enter the size of the list"))

# Print a message to prompt the user to enter elements
print("enter element to list")

# Initialize two empty lists
l = []
a = []

# Loop through the range of the list size
for i in range(n):
    # Get an integer input from the user and append it to list l
    a = int(input())
    l.append(a)

# Assign list l to list a (making a copy of list l)
a = l

# Sort list a in ascending order
a.sort()

# Print the sorted list a
print(a)

# Check if list a is equal to list l (i.e., if the original list was already sorted)
if (a == l):
    # If they are equal, print that the given list is not in ascending order (because it was already sorted)
    print("the given list is not in ascending order")
else:
    # If they are not equal, print that the given list is in ascending order
    print("the given list is in ascending order")