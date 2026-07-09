import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame(
    np.random.randint(1, 21, size=(3, 3)),
    columns=['A', 'B', 'C'],
    index=['X', 'Y', 'Z']
)

print("DataFrame:")
print(df)

# Access element at row Y and column B
element = df.loc['Y', 'B']

print("\nElement at row 'Y' and column 'B':")
print(element)