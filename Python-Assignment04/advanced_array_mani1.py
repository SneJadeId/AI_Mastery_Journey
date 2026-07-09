import numpy as np

# Create a 3x3 array with values from 1 to 9
array = np.arange(1, 10).reshape(3, 3)

print("Original Array:")
print(array)

# Reshape to 1x9
array_1x9 = array.reshape(1, 9)

print("\nReshaped to (1, 9):")
print(array_1x9)

# Reshape to 9x1
array_9x1 = array.reshape(9, 1)

print("\nReshaped to (9, 1):")
print(array_9x1)