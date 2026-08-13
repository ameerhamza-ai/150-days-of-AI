sentence = "I love Python and AI and Machine Learning"

# 1. Split sentence into a list of words
all_words = sentence.split()

# 2. Filter words with 3+ letters, remove duplicates (unique), and sort alphabetically
# Using set() removes duplicates automatically
filtered_sorted_words = sorted(list({w for w in all_words if len(w) >= 3}))

print(filtered_sorted_words)
