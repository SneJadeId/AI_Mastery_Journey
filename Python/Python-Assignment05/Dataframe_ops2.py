import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame(
    np.random.randint(1, 21, size=(4, 3)),
    columns=['A', 'B', 'C']
)

print("Original DataFrame:")
print(df)

# Row-wise sum
df['Row_Sum'] = df.sum(axis=1)

print("\nDataFrame with Row-wise Sum:")
print(df)

# Column-wise sum
column_sum = df[['A', 'B', 'C']].sum(axis=0)

print("\nColumn-wise Sum:")
print(column_sum)