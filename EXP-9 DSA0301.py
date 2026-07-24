import re

# Input sentence
sentence = "John is running with 5 dogs"

words = sentence.split()

print("Rule-Based POS Tagging using Regular Expressions\n")

for word in words:

    if re.fullmatch(r"[0-9]+", word):
        tag = "CD"      # Cardinal Number

    elif re.fullmatch(r".*ing", word):
        tag = "VBG"     # Verb (Gerund)

    elif re.fullmatch(r".*ed", word):
        tag = "VBD"     # Verb (Past Tense)

    elif re.fullmatch(r".*ly", word):
        tag = "RB"      # Adverb

    elif word.lower() in ["is", "am", "are", "was", "were"]:
        tag = "VB"

    elif word.lower() in ["with", "in", "on", "at", "to"]:
        tag = "IN"      # Preposition

    elif word[0].isupper():
        tag = "NNP"     # Proper Noun

    else:
        tag = "NN"      # Noun

    print(word, "->", tag)
