# 1. Squares from 1 to 10
squares = [i ** 2 for i in range(1,11)]
print(f"Squares (1-10): {squares}")

# 2. Even numbers from 1 to 20
even = [i for i in range(1,21) if i%2==0]
print(f"Even (1-20): {even}")

# 3. Words with 5+ letters from a words list
words_list = ["apple", "banana", "kiwi", "cherry", "fig", "grapefruit"]
long_words = [word for word in words_list if len(word) >= 5]
print("Words with 5+ letters:", long_words)