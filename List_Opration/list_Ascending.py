# Initialize a list 'l' with integers and an integer variable 'k' set to 0
l = [21, 22, 23, 69, 77]
k = 0

# Iterate through the list using a for loop, with 'i' as the index
for i in range(5):
    
    # Check if the current iteration is the second-to-last index
    if(i == 4):
        
        # If so, break the loop to avoid an IndexError
        break
    
    # Compare the current element with the next element in the list
    if(l[i] > l[i+1]):
        
        # If the current element is greater than the next one, increment 'k' by 1
        k = k + 1
        
        # Break the loop since the list is not in ascending order
        break

# Check if 'k' is equal to 1
if(k == 1):
    
    # If so, print "not in ascending order"
    print("not in ascending order")
else:
    
    # Otherwise, print "yes in ascending order"
    print("yes in ascending order")