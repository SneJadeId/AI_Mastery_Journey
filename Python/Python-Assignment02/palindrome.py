def is_palindrome(s):
    # Keep only letters and digits, and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]


# Input
text = input("Enter a string: ")

# Output
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")