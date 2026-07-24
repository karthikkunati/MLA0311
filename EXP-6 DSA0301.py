from collections import defaultdict
import random

# Training text
text = """
I love NLP
I love Python
I love AI
You love NLP
You love Python
"""

# Tokenize
words = text.split()

# Build Bigram Model
bigram = defaultdict(list)

for i in range(len(words) - 1):
    bigram[words[i]].append(words[i + 1])

# Generate text
start_word = "I"
generated = [start_word]
current = start_word

for _ in range(10):
    if current not in bigram:
        break
    next_word = random.choice(bigram[current])
    generated.append(next_word)
    current = next_word

print("Generated Text:")
print(" ".join(generated))
