# Read the number of lines to be read from the user
n = int(input("enter the number of lines to be read"))

# Open the file "pr.txt" in read mode
f = open("pr.txt", "r")

# Loop through the file and read 'n' number of lines
for i in range(n):
    # Print each line
    print(f.readline())

# Close the file
f.close()