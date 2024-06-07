# Take input from the user and store it in the variable 's'
s=input("enter the string")

# Split the input string into a list of words and store it in the variable 'sp'
sp=s.split()

# Calculate the length of the list 'sp' and store it in the variable 'l'
l=len(sp)

# Initialize an empty list 'ln' to store the frequency of each word
ln=[]

# Iterate over the range of the length of 'sp'
for i in range(0,l):
    # Count the frequency of the word at index 'i' in the list 'sp' and store it in the variable 'n'
    n=sp.count(sp[i])
    # Append the frequency 'n' to the list 'ln'
    ln.append(n)

# Iterate over the range of the length of 'sp' again
for i in range(0,l):
    # Check if the frequency of the word at index 'i' is less than or equal to 1
    if(ln[i]<=1):
        # Print the word at index 'i' if its frequency is less than or equal to 1
        print(sp[i])