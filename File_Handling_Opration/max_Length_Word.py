# Open the file "pr.txt" in read mode
f=open("pr.txt","r")

# Initialize an empty list to store the data
ar=[]

# Read the entire file and store it in the list
ar=f.read()

# Split the string into individual words using the split() function
w=ar.split()

# Calculate the total number of words
l=len(w)

# Initialize the maximum length and the corresponding word
max=0
m=""

# Iterate through each word in the list
for i in w:
    # Calculate the length of the current word
    ln=len(i)
    
    # Check if the length of the current word is greater than the maximum length found so far
    if(ln>max):
        # Update the maximum length and the corresponding word
        max=ln
        m=i

# Print the word with the maximum length
print(m)

# Close the file
f.close()