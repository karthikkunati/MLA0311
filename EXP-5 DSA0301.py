# EXP-5: Simple Word Stemmer (Without NLTK)

def stem(word):

    if word.endswith("ing"):
        return word[:-3]

    elif word.endswith("ed"):
        return word[:-2]

    elif word.endswith("ies"):
        return word[:-3] + "y"

    elif word.endswith("es"):
        return word[:-2]

    elif word.endswith("s"):
        return word[:-1]

    elif word.endswith("ness"):
        return word[:-4]

    else:
        return word

# List of words
words = ["running", "playing", "studies", "connected", "boxes", "cars", "happiness"]

print("Word Stemming\n")

for word in words:
    print(word, "->", stem(word))
