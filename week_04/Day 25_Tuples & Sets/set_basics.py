# 1. Create a set of fruits (Sets use curly braces {})
fruits = {"apple", "banana", "mango"}
print(f"Original Set: {fruits}")

# 2. Add a duplicate and observe
fruits.add("apple")
print(f"After adding duplicate 'apple': {fruits} (No change!)")

# 3. Use add() to add a new item
fruits.add("orange")
print(f"After add('orange'): {fruits}")

# 4. Use remove() to delete an item
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# 5. Use discard() on a missing item
# remove() throws an error if item is missing, but discard() is safe!
fruits.discard("grapes")
print(f"After discard('grapes'): {fruits} (No error occurred)")