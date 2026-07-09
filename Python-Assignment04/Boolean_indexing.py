import numpy as np

# Create a 4x4 array with random integers from 1 to 20
array = np.random.randint(1, 21, size=(4, 4))

print("Original Array:")
print(array)

# Replace all elements greater than 10 with 10
array[array > 10] = 10

print("\nModified Array:")
print(array)