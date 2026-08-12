words = ["python", "ai", "machine", "learning", "deep", "data"]

# 1. Convert all words to upper case
upper_words = [w.upper() for w in words]

# 2. Get the length of each word
word_lengths = [len(w) for w in words]

# 3. Filter words that have 4 or more letters
long_words = [w for w in words if len(w) >= 4]

# 4. Reverse each word in the list
reversed_words = [w[::-1] for w in words]

print("Upper:", upper_words)
print("Lengths:", word_lengths)
print("4+ Letters:", long_words)
print("Reversed:", reversed_words)
