import numpy as np

# Create a 5x5 array with random integers from 1 to 20
arr = np.random.randint(1, 21, size=(5, 5))

print("Original Array:")
print(arr)

print("\nBorder Elements:")

# Top row
print("Top Row:", arr[0])

# Bottom row
print("Bottom Row:", arr[-1])

# Left column (excluding corners)
print("Left Column:", arr[1:-1, 0])

# Right column (excluding corners)
print("Right Column:", arr[1:-1, -1])