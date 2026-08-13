# 1. Create the numbers dictionary
# (I mixed the order of keys here so we can clearly see the sorting work later)
numbers_dict = {"d": 40, "a": 10, "c": 30, "b": 20}
print(f"Original Dictionary: {numbers_dict}\n")

# 2. Sum of all values
# sum() adds up all the numbers, and .values() gets only the numbers from the dict
total_sum = sum(numbers_dict.values())
print(f"Sum of all values: {total_sum}")

# 3. Find the key with the maximum value
# max() usually checks keys, but 'key=numbers_dict.get' tells it to check based on the values
max_key = max(numbers_dict, key=numbers_dict.get)
print(f"Key with the MAXIMUM value: '{max_key}' (which is {numbers_dict[max_key]})")

# 4. Find the key with the minimum value
min_key = min(numbers_dict, key=numbers_dict.get)
print(f"Key with the MINIMUM value: '{min_key}' (which is {numbers_dict[min_key]})")

# 5. Sort keys alphabetically
# sorted() takes the keys and returns them in A-Z alphabetical order as a list
sorted_keys = sorted(numbers_dict.keys())
print(f"Alphabetically sorted keys: {sorted_keys}")