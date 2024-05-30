import numpy as np  # Import the NumPy library and assign it the alias 'np'

# Create a 1-dimensional NumPy array with 10 elements
arr4 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Reshape the array into a 2-dimensional array with 2 rows and 5 columns
arr4 = arr4.reshape(2, 5)

# Print the reshaped array
print(arr4)