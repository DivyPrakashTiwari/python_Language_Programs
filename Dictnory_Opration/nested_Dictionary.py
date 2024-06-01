# Create three dictionaries to store information about three children
child1 = {"name": "shikha", "dob": 2001}  # child1's information
child2 = {"name": "nisha", "dob": 2002}  # child2's information
child3 = {"NAME": "DIVY", "ROLL": "CSF21034", "REGD": 2101020449, "BRANCH": "CSF"}  # child3's information

# Create a dictionary to store the three children
myfam = {"child1": child1, "child2": child2, "child3": child3}  # myfam dictionary to store child1, child2, and child3

# Print the myfam dictionary
print("Initial myfam dictionary:")
print(myfam)

# Update the myfam dictionary to store the name of child1, keys of child2, and values of child3
myfam = {"child1": child1["name"], "child2": list(child2.keys()), "child3": list(child3.values())}  # update myfam dictionary

# Print the updated myfam dictionary
print("\nUpdated myfam dictionary (name of child1, keys of child2, and values of child3):")
print(myfam)

# Update the child1 dictionary to change the name to "shikha ranjan"
child1.update({"name": "shikha ranjan"})  # update child1's name

# Update the myfam dictionary to store the updated child1, items of child2, and values of child3
myfam = {"child1": child1, "child2": list(child2.items()), "child3": list(child3.values())}  # update myfam dictionary

# Print the updated myfam dictionary
print("\nUpdated myfam dictionary (updated child1, items of child2, and values of child3):")
print(myfam)

# Update the myfam dictionary to store the result of updating child1, items of child2, and values of child3
# Note: The update method returns None, so child1 will be None in the myfam dictionary
myfam = {"child1": child1.update({"name": "shikha ranjan"}), "child2": list(child2.items()), "child3": list(child3.values())}  # update myfam dictionary

# Print the updated myfam dictionary
print("\nUpdated myfam dictionary (result of updating child1, items of child2, and values of child3):")
print(myfam)

# Print a blank line
print()