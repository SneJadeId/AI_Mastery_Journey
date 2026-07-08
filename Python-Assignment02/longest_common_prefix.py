def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


# Input
strings = input("Enter words separated by spaces: ").split()

# Output
print("Longest Common Prefix:", longest_common_prefix(strings))