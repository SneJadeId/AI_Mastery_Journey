import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame(
    np.random.randint(1, 11, size=(5, 3)),
    columns=['A', 'B', 'C']
)

print("Original DataFrame:")
print(df)

# Add new column
df['Product'] = df['A'] * df['B']

print("\nDataFrame after adding Product column:")
print(df)