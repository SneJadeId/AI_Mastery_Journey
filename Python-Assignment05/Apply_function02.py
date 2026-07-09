import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame(
    np.random.randint(1, 21, size=(6, 3)),
    columns=['A', 'B', 'C']
)

print("Original DataFrame:")
print(df)

# Create a new column that is the sum of A, B, and C
df['Total'] = df.apply(lambda row: row['A'] + row['B'] + row['C'], axis=1)

print("\nDataFrame with Total Column:")
print(df)