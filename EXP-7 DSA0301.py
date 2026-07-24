# EXP-7: Simple POS Tagging (Without NLTK)

sentence = "John works at Google."

# Remove the period and split into words
words = sentence.replace(".", "").split()

# Simple POS dictionary
pos_tags = {
    "John": "NNP",      # Proper Noun
    "works": "VBZ",     # Verb
    "at": "IN",         # Preposition
    "Google": "NNP"     # Proper Noun
}

print("Part-of-Speech Tags:\n")

for word in words:
    print(f"{word} --> {pos_tags.get(word, 'NN')}")
