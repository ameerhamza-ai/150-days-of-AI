sentence = "I love Python and Python loves AI and I love AI"

# 1. Split the sentence into a list of separate words
# .split() breaks the string at every space
words_list = sentence.split()

# 2. Count each word using a dictionary
word_counts = {}

for word in words_list:
    if word in word_counts:
        # If the word is already in the dictionary, increase its count by 1
        word_counts[word] += 1
    else:
        # If it's a new word, add it to the dictionary with a count of 1
        word_counts[word] = 1

print("--- Word Count Dictionary ---")
print(word_counts)
print("\n-----------------------------\n")

# 3. Find the most repeated word
# max() will check the dictionary values using .get and return the top key.
# Note: Since many words appear 2 times, max() will return the first one it finds.
most_repeated = max(word_counts, key=word_counts.get)
max_count = word_counts[most_repeated]

print(f"Most repeated word: '{most_repeated}' (appears {max_count} times)")

# 4. Count of unique words
# Dictionaries only store unique keys, so the total number of keys is the unique word count
unique_words_count = len(word_counts)

print(f"Total unique words count: {unique_words_count}")