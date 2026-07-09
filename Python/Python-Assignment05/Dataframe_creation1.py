import pandas as pd
import numpy as np

# Create a DataFrame with 6 rows and 4 columns
data = np.random.randint(1, 21, size=(6, 4))

df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

print("Original DataFrame:")
print(df)

# Set the first column as the index
df.set_index('A', inplace=True)

print("\nDataFrame after setting column 'A' as index:")
print(df)