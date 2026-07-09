import pandas as pd
import numpy as np

# Create a DataFrame with random integers
df = pd.DataFrame(
    np.random.randint(1, 21, size=(6, 4)),
    columns=['A', 'B', 'C', 'D']
)

# Introduce NaN values
df.iloc[2, 1] = np.nan
df.iloc[4, 3] = np.nan

print("Original DataFrame:")
print(df)

# Drop rows containing NaN values
df_clean = df.dropna()

print("\nDataFrame after dropping rows with NaN values:")
print(df_clean)