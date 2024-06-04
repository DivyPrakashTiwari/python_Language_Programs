# Get the size of the list from the user
n = int(input("Enter the size of the list"))

# Print a message to prompt the user to enter elements
print("enter element to list")

# Initialize an empty list to store the elements
l = []

# Loop to get 'n' number of elements from the user
for i in range(n):
    # Get an integer input from the user
    a = int(input())
    
    # Append the input to the list
    l.append(a)

# Print a message to indicate the start of even numbers
print("even numbers are")

# Loop through the list to find and print even numbers
for i in range(n):
    # Check if the current element is even (i.e., divisible by 2)
    if (l[i] % 2 == 0):
        # Print the even number
        print(l[i])