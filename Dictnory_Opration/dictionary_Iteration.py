# Defining a dictionary 'dict' with personal information
dict = {"NAME": "DIVY", "ROLL": "CSF21034", "REGD": 2101020449, "BRANCH": "CSF"}

# Printing the entire dictionary
print(dict)

# Iterating through the keys of the dictionary
for x in dict:
    # Printing each key
    print(x)

# Iterating through the keys of the dictionary again
for x in dict:
    # Printing the value associated with each key
    print(dict[x])

# Creating a shallow copy of the dictionary 'dict' and storing it in 'dict1'
dict1 = dict.copy()

# Printing the copied dictionary 'dict1'
print(dict1)