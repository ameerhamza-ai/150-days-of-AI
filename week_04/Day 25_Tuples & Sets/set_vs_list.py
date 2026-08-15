numbers_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(f"Original List with duplicates: {numbers_list}")

# 1. Remove duplicates using a set
unique_set = set(numbers_list)
print(f"Duplicates removed (Set): {unique_set}")

# 2. Count unique elements
unique_count = len(unique_set)
print(f"Total unique elements: {unique_count}")

# 3. Convert set back to list
back_to_list = list(unique_set)

# 4. Return sorted list (Sets don't maintain order, so it's good to sort)
sorted_unique_list = sorted(back_to_list)
print(f"Final Sorted Unique List: {sorted_unique_list}")