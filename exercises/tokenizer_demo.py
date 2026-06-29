# tokenizer_demo.py

sentence = "The cat sat on the mat."

# Python sees this as a raw string
print("Raw text:")
print(sentence)

print("\nCharacters:")
for char in sentence:
    print(char)

print("\nSimple tokenization (split by spaces):")
tokens = sentence.split()

print(tokens)