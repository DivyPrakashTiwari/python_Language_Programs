# Initialize a list of integers
lis = [11, 21, 30, 29, 55, 7, 69, 10]

# Initialize maximum value as 0
ma = 0

# Initialize minimum value as the first element of the list
mi = lis[0]

# Iterate over the list using a for loop
for i in range(0, 8):
    # Check if the current element is greater than or equal to the maximum value
    if (ma <= lis[i]):
        # Update the maximum value
        ma = lis[i]
    # Check if the current element is less than or equal to the minimum value
    elif (mi >= lis[i]):
        # Update the minimum value
        mi = lis[i]
    # If the current element is neither the maximum nor the minimum, skip it
    else:
        continue
    # Increment the loop counter (not necessary in this case, as the loop will iterate automatically)
    i = i + 1

# Print the maximum value
print("maximum ", ma)

# Print the minimum value
print("minimum ", mi)