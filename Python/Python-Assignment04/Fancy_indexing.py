import numpy as np

# Create a 5x5 array with random integers from 1 to 20
array = np.random.randint(1, 21, size=(5, 5))

print("Original Array:")
print(array)

# Fancy indexing to extract the four corners
corners = array[[0, 0, 4, 4], [0, 4, 0, 4]]

print("\nCorner Elements:")
print(corners)