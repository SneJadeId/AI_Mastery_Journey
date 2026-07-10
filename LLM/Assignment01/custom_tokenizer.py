import re

class SimpleTokenizer:

    def __init__(self):
        self.vocabulary = {}
        self.next_id = 1

    def tokenize(self, text):

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        # Split into words
        tokens = text.split()

        return tokens

    def build_vocabulary(self, tokens):

        token_ids = []

        for token in tokens:

            if token not in self.vocabulary:
                self.vocabulary[token] = self.next_id
                self.next_id += 1

            token_ids.append(self.vocabulary[token])

        return token_ids


# -------------------------------
# Main Program
# -------------------------------

tokenizer = SimpleTokenizer()

text = input("Enter one or more sentences:\n")

tokens = tokenizer.tokenize(text)

token_ids = tokenizer.build_vocabulary(tokens)

print("\nTokens:")
print(tokens)

print("\nVocabulary:")
print(tokenizer.vocabulary)

print("\nToken IDs:")
print(token_ids)