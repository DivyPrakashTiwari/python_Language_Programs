# Open the file "P.txt" in read mode
f=open("C:\\Users\\DIVY PRAKASH TIWARI\\Desktop\\P.txt","r")

# Print the content of the file
print(f.read())

# Close the file (not done, but recommended)

# Open the file "P.txt" in write mode, this will overwrite the existing content
f=open("C:\\Users\\DIVY PRAKASH TIWARI\\Desktop\\P.txt","w")

# Write a new string to the file
f.write("arre baap re delete ho gaya suub")

# Open the file "P.txt" in read mode again
f=open("C:\\Users\\DIVY PRAKASH TIWARI\\Desktop\\P.txt","r")

# Print the new content of the file
print(f.read())

# Close the file
f.close()