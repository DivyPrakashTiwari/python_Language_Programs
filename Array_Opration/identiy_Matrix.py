# Import the numpy library and assign it the alias 'np' for convenience.
import numpy as np

# Create a 2-dimensional array with ones on the main diagonal and zeros elsewhere.
# The 'eye' function is used to create an identity array, and the argument '4' specifies the number of rows (and columns).
arr1 = np.eye(4)

# Print the resulting 4x4 array to the console.
print(arr1)