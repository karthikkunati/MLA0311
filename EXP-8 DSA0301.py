import random

# Training data: possible POS tags for each word
tag_dictionary = {
    "John": ["NNP"],
    "works": ["VBZ", "NNS"],   # Can be verb or plural noun
    "at": ["IN"],
    "Google": ["NNP"],
    "play": ["VB", "NN"],
    "book": ["NN", "VB"],
    "is": ["VBZ"],
    "good": ["JJ"]
}

# Input sentence
sentence = "John works at Google"

words = sentence.split()

print("Stochastic POS Tagging\n")

# Assign a random tag from the possible tags
for word in words:
    if word in tag_dictionary:
        tag = random.choice(tag_dictionary[word])
    else:
        tag = "NN"   # Default tag
    print(word, "->", tag)
