def to_camel_case(text):
    words = text.split()

    if not words:
        return ""

    camel_case = words[0].lower()

    for word in words[1:]:
        camel_case += word.capitalize()

    return camel_case


# Input
text = input("Enter a sentence: ")

# Output
print("CamelCase:", to_camel_case(text))