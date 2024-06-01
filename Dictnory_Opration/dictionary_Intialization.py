# Define a dictionary with personal information
dict = {"NAME": "DIVY", "ROLL": "CSF21034", "REGD": 2101020449, "BRANCH": "CSF"}

# Print the dictionary
print(dict)

# Print the type of the dictionary
print(type(dict))

# Print the values of the dictionary
print(dict.values())

# Print the keys of the dictionary
print(dict.keys())

# Print the items (key-value pairs) of the dictionary
print(dict.items())

# Print the value of the key "NAME"
print(dict["NAME"])

# Add a new key-value pair to the dictionary
dict["ADDitem"] = "xyz"

# Update the value of the key "ROLL"
dict.update({"ROLL": "CSESF21034"})

# Print the updated dictionary
print(dict)

# Remove the key-value pair with the key "ADDitem"
dict.pop("ADDitem")

# Print the dictionary after removing the key-value pair
print(dict)

# Remove the last key-value pair from the dictionary
dict.popitem()

# Print the dictionary after removing the last key-value pair
print(dict)

# Attempt to print the dictionary after deleting it
del dict

# Print the dictionary after deleting it (this will raise an error)
# print(dict)