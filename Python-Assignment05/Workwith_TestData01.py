import pandas as pd

# Create a Series of text strings
text = pd.Series([
    'python',
    'pandas',
    'machine',
    'learning',
    'data'
])

print("Original Series:")
print(text)

# Convert to uppercase
uppercase = text.str.upper()

print("\nUppercase Strings:")
print(uppercase)