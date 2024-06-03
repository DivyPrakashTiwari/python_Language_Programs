# Open the file 'P.txt' located on the user's desktop in read mode
f = open("C:\\Users\\DIVY PRAKASH TIWARI\\Desktop\\P.txt","r")

# Read the first 20 characters from the file
print(f.read(20))

# Close the file to free up system resources
f.close