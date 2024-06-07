# Take input from the user and store it in the variable 's'
s=input("enter the string")

# Split the input string into a list of words and store it in the variable 'sp'
sp=s.split()

# Calculate the total number of words in the input string and store it in the variable 'l'
l=len(sp)

# Initialize an empty list 'ln' to store the length of each word
ln=[]

# Iterate over each word in the list 'sp' and calculate its length
for i in range(0,l):
    # Append the length of the current word to the list 'ln'
    ln.append(len(sp[i]))

# Initialize a variable 'm' to store the maximum length of a word
m=0

# Initialize a variable 'n' to store the index of the word with maximum length
n=0

# Iterate over each word in the list 'sp' to find the word with maximum length
for i in range(0,l):
    # Check if the length of the current word is greater than the maximum length found so far
    if(m<int(ln[i])):
        # Update the maximum length and the index of the word with maximum length
        m=ln[i]
        n=i

# Print the word with maximum length
print("the largest word is ",sp[n])