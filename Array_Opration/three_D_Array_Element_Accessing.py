import numpy as np

# Create a 3D numpy array 'arr3' with shape (3, 3, 4)
arr3 = np.array([[[10,20,30,40],[1,2,3,4],[1.1,2.2,3.3,4.4]],
                 [[11,22,33,44],[111,222,333,444],[11.1,22.2,33.3,44.4]],
                 [[100,200,300,400],[101,201,301,401],[1.11,2.22,3.33,4.44]]])

# Print the 3D array 'arr3'
print (arr3)

# Access and print the element at index (1, 1, 3) of 'arr3'
print (arr3[1,1,3])

# Print the shape of 'arr3'
print(arr3.shape)