import pandas as pd
import numpy as np

# Create MultiIndex
index = pd.MultiIndex.from_tuples([
    ('A', 1),
    ('A', 2),
    ('B', 1),
    ('B', 2),
    ('C', 1),
    ('C', 2)
], names=['Category', 'Number'])

# Create DataFrame
df = pd.DataFrame({
    'Value': np.random.randint(10, 100, size=6)
}, index=index)

print("MultiIndex DataFrame:")
print(df)

# Access all rows of Category A
print("\nRows of Category A:")
print(df.loc['A'])

# Access a specific row
print("\nRow (B,2):")
print(df.loc[('B', 2)])

# Slice Categories A to B
print("\nRows from Category A to B:")
print(df.loc['A':'B'])