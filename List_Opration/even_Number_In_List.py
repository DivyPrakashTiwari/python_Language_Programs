# This is a Python list containing integers
l = [24, 21, 69, 32, 47]

# Print the string "even numbers are" to the console
print("even numbers are")

# Iterate through the first 4 elements of the list 'l'
for i in range(4):
    
    # Check if the current element is even by taking its remainder when divided by 2
    if l[i] % 2 == 0:
        
        # Print the current even element to the console
        print(l[i])