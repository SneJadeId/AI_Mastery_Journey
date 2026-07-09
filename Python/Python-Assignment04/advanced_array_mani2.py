import numpy as np

# Create a 5x5 array with random integers from 1 to 20
array = np.random.randint(1, 21, size=(5, 5))

print("Original Array:")
print(array)

# Flatten the array
flattened = array.flatten()

print("\nFlattened Array:")
print(flattened)

# Reshape back to 5x5
reshaped = flattened.reshape(5, 5)

print("\nReshaped Array:")
print(reshaped)