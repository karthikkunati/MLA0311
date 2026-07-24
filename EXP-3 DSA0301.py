# EXP-3: Morphological Analysis (Without NLTK)

words = ["running", "played", "cars", "studies", "boxes"]

print("Morphological Analysis\n")

for word in words:

    if word.endswith("ing"):
        root = word[:-3]

    elif word.endswith("ed"):
        root = word[:-2]

    elif word.endswith("ies"):
        root = word[:-3] + "y"

    elif word.endswith("es"):
        root = word[:-2]

    elif word.endswith("s"):
        root = word[:-1]

    else:
        root = word

    print(word, "->", root)
