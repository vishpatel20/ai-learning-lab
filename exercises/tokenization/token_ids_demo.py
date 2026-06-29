# exercises/tokenization/token_ids_demo.py

text = "Hello AI hello world AI"

# Step 1: Tokenize
tokens = text.split()

print("Tokens:")
print(tokens)

# Step 2: Build vocabulary
vocab = {}
id_counter = 0

for token in tokens:
    if token not in vocab:
        vocab[token] = id_counter
        id_counter += 1

print("\nVocabulary:")
print(vocab)

# Step 3: Convert tokens to IDs
token_ids = [vocab[token] for token in tokens]

print("\nToken IDs:")
print(token_ids)