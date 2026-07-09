import pandas as pd
import numpy as np

# Create a DataFrame with 5 rows and 3 columns
df = pd.DataFrame(
    np.random.randint(1, 21, size=(5, 3)),
    columns=['A', 'B', 'C']
)

print("Original DataFrame:")
print(df)

# Apply a function to double every value
df_double = df.apply(lambda x: x * 2)

print("\nDataFrame after Doubling the Values:")
print(df_double)