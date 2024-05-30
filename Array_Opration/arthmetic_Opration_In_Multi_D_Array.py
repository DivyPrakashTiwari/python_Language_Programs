import numpy as np

# Define two numpy arrays arr1 and arr2 with the same shape
arr1 = np.array([[[10,20,30,40],[1,2,3,4],[1.1,2.2,3.3,4.4]],
                 [[11,22,33,44],[111,222,333,444],[11.1,22.2,33.3,44.4]],
                 [[100,200,300,400],[101,201,301,401],[1.11,2.22,3.33,4.44]]])

arr2 = np.array([[[10,20,30,40],[1,2,3,4],[1.1,2.2,3.3,4.4]],
                 [[11,22,33,44],[111,222,333,444],[11.1,22.2,33.3,44.4]],
                 [[100,200,300,400],[101,201,301,401],[1.11,2.22,3.33,4.44]]])

# Perform element-wise addition of arr1 and arr2, storing the result in arr3
arr3 = arr1 + arr2

# Perform element-wise subtraction of arr2 from arr1, storing the result in arr4
arr4 = arr1 - arr2

# Perform element-wise multiplication of arr1 and arr2, storing the result in arr5
arr5 = arr1 * arr2

# Perform element-wise integer division of arr1 by arr2, storing the result in arr6
arr6 = arr1 // arr2

# Print the resulting arrays
print(arr3)
print(arr4)
print(arr5)
print(arr6)