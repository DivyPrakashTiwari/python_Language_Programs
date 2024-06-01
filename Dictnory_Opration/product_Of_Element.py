# Initialize a dictionary 'dict' with key-value pairs where keys are integers from 1 to 4 and values are their respective cube values
dict = {1: 7, 2: 4, 3: 29, 4: 11}

# Initialize a variable 'p' and assign it the value 1
p = 1

# Iterate through the range of integers from 1 to 4 (inclusive)
for i in range(1, 5):
    # Get the cube value of the current integer 'i' from the dictionary
    n = dict[i]
    # Multiply the variable 'p' with the cube value of 'i' and update the value of 'p'
    p = p * n

# Print the final value of 'p' after the loop
print(p)

# Reset the variable 'p' to 1
p = 1

# Iterate through the dictionary keys
for i in dict:
    # Multiply the variable 'p' with the cube value of the current key 'i' from the dictionary and update the value of 'p'
    p = p * dict[i]

# Print the final value of 'p' after the loop
print(p)