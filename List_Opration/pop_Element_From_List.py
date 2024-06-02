# Initialize a list 'lis' with some integer values
lis = [1, 2, 3, 2, 5, 7, 9, 10, 11]

# Loop through the list using variable 'i' as the index, starting from 0 up to (but not including) the length of the list
for i in range(len(lis)):
    
    # Nested loop through the list using variable 'j' as the index, starting from 1 up to (but not including) the length of the list
    for j in range(1, len(lis)):
        
        # Check if the value at index 'i' is equal to the value at index 'j'
        if lis[i] == lis[j]:
            
            # If the values are equal, remove the element at index 'i' from the list
            lis.pop(i)

# Print the modified list
print(lis)