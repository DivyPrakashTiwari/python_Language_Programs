# Take input from the user for two strings
s1=input("enter the 1 string")
s2=input("enter the 2 string")

# Convert both strings to lowercase to ensure case-insensitive comparison
s1.lower()
s2.lower()

# Calculate the length of both strings
l1=len(s1)
l2=len(s2)

# Initialize an empty list to store common elements
ln=[]

# Print a message to indicate the start of common elements
print("common elements are")

# Iterate over each character in the first string
for i in range(0,l1):
    # Iterate over each character in the second string
    for j in range(0,l2):
        # Check if the current characters in both strings are equal
        if(s1[i]==s2[j]):
            # If they are equal, add the character to the list of common elements
            ln.append(s1[i])

# Calculate the length of the list of common elements
ln1=len(ln)

# Iterate over the list of common elements
for i in range(0,ln1):
    # Print each common element
    print(ln[i])
    # Increment the counter (although this increment is unnecessary in this case)
    i=i+1