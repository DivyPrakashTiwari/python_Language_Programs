# Initialize two lists, lis and lista, with integers
lis = [111, 29, 30, 21, 55, 10, 69, 7]
lista = [29, 11, 7, 12, 247, 17, 10, 3]

# Iterate over the indices of lis using a for loop
for i in range(0, 8):
    # Iterate over the indices of lista using a nested for loop
    for j in range(0, 8):
        # Check if the current element in lis is equal to the current element in lista
        if (lis[i] == lista[j]):
            # If the elements are equal, store the value in a variable a
            a = lis[i]
            # Print the common element
            print(lis[i])
            # Increment j by 1 to skip the current iteration in the inner loop
            j = j + 1
    # Increment i by 1 to move to the next iteration in the outer loop
    i = i + 1