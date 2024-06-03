# Open the file "p.txt" in read and write mode
f=open("p.txt","r+")
 
# Read the contents of the file and print it
print(f.read())
 
# Write the string "jai ho" to the file
f.write("jai ho")
 
# Try to read the contents of the file again, but this will not work as expected
# because the file pointer is at the end of the file after the write operation
print(f.read())
 
# Close the file
f.close()