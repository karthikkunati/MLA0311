# EXP-10: Transformation-Based POS Tagging

# Input sentence
words = ["I", "can", "play", "cricket"]

# Initial POS tags (before applying rules)
tags = ["PRP", "NN", "NN", "NN"]

print("Before Transformation:")
for i in range(len(words)):
    print(words[i], "->", tags[i])

# Transformation Rules
for i in range(len(words)):

    # Rule 1: "can" is a modal verb
    if words[i].lower() == "can":
        tags[i] = "MD"

    # Rule 2: "play" is a verb
    elif words[i].lower() == "play":
        tags[i] = "VB"

    # Rule 3: Pronouns
    elif words[i].lower() in ["i", "you", "he", "she", "we", "they"]:
        tags[i] = "PRP"

print("\nAfter Transformation:")
for i in range(len(words)):
    print(words[i], "->", tags[i])
