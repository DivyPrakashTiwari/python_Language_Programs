import numpy as np  # Import the NumPy library and assign it the alias 'np'

# Create a 2-dimensional NumPy array with three rows and four columns
arr2 = np.array([[10,20,30,40],[1,2,3,4],[1.1,2.2,3.3,4.4]])

# Print the entire array
print(arr2)

# Access the element at the 3rd row and 2nd column (Python uses 0-based indexing, so 2nd column is at index 1)
n = arr2[2,1]

# Print the accessed element
print(n)

# Print the shape of the array, which represents the number of rows and columns
print(arr2.shape)