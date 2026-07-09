import numpy as np

# Create a 6x6 array with values from 1 to 36
arr = np.arange(1, 37).reshape(6, 6)

print("Original Array:")
print(arr)

# Extract the 3rd to 5th rows and 2nd to 4th columns
sub_array = arr[2:5, 1:4]

print("\nExtracted Sub-array:")
print(sub_array)