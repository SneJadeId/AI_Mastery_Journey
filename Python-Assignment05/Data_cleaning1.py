import pandas as pd
import numpy as np

# Create a DataFrame with random integers
df = pd.DataFrame(
    np.random.randint(1, 21, size=(5, 3)),
    columns=['A', 'B', 'C']
)

# Introduce NaN values
df.iloc[1, 0] = np.nan
df.iloc[3, 2] = np.nan

print("Original DataFrame:")
print(df)

# Fill NaN values with column mean
df = df.fillna(df.mean())

print("\nDataFrame after filling NaN values with column mean:")
print(df)