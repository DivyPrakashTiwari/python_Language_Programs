# Define two dictionaries, dict1 and dict2, with integer keys and values
dict1 = {1: 1, 2: 2, 3: 3, 4: 4}
dict2 = {11: 11, 22: 22, 33: 33, 44: 44}

# Update dict1 by adding the key-value pairs from dict2
# This will overwrite any existing keys in dict1 that also exist in dict2
dict1.update(dict2)

# Print the updated dict1
print(dict1)