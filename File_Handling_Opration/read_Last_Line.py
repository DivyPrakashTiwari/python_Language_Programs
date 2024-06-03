# Open the file "pr.txt" in read mode and store the reference in variable 'f'
f = open("pr.txt", "r")

# Initialize an empty list 'ar' to store the lines read from the file
ar = []

# Read 5 lines from the file and append each line to the list 'ar'
for i in range(5):
    ar.append(f.readline())

# Calculate the length of the list 'ar' and store it in variable 'l'
l = len(ar)

# Print the last line read from the file, which is the (l-1)th element of the list 'ar'
print(ar[l-1])

# Close the file after reading to free up system resources
f.close()