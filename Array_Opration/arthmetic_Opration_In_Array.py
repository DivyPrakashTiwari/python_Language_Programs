import numpy as np

# Create two numpy arrays arr1 and arr2
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

# Add arr1 and arr2, store the result in arr3
arr3 = arr1 + arr2
# Subtract arr2 from arr1, store the result in arr4
arr4 = arr1 - arr2
# Multiply arr1 and arr2 element-wise, store the result in arr5
arr5 = arr1 * arr2
# Floor divide arr1 by arr2 element-wise, store the result in arr6
arr6 = arr1 // arr2

# Print the resulting arrays
print(arr3)
print(arr4)
print(arr5)
print(arr6)