# Finite State Machine for Morphological Parsing
# Generate plural forms of English nouns

def plural(noun):

    # Rule 1: Nouns ending with 'y'
    if noun.endswith("y"):
        return noun[:-1] + "ies"

    # Rule 2: Nouns ending with s, x, z, ch, sh
    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    # Rule 3: Other nouns
    else:
        return noun + "s"

# List of nouns
words = ["cat", "baby", "box", "bus", "church"]

print("Plural Forms:\n")

for word in words:
    print(word, "->", plural(word))
