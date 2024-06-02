n = int(input("enter the number of element in list"))  # Get the number of elements in the list from the user
l = []  # Initialize an empty list to store the elements
s = 0  # Initialize a variable s, but it's not used anywhere in the code

print("enter the element to the list")  # Prompt the user to enter the elements
for i in range(0, n):  # Loop to get 'n' number of elements from the user
    a = int(input())  # Get an integer input from the user
    l.append(a)  # Add the input to the list

for w in range(0, n):  # Loop to remove duplicates from the list
    for j in range(w + 1, n):  # Inner loop to compare each element with the rest
        if (l[w] == l[j]):  # Check if the current element is equal to any other element
            l.pop(w)  # Remove the duplicate element
        j = j + 1  # Increment the inner loop counter
    i = i + 1  # Increment the outer loop counter, but it's not necessary

for k in range(n - 1):  # Loop to print the elements in the list
    print(l[k])  # Print each element in the list
    i = i + 1  # Increment a variable, but it's not used anywhere