numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]

# 1. Sort 
numbers.sort()
print("Sorted List:", numbers)

# 2. Reverse 
numbers.reverse()
print("Reversed List:", numbers)

# Note: The list has changed because of the reverse operation, 
# so we are defining the same list again to check the index and count on the original list.
original_list = [5, 3, 8, 1, 9, 2, 7, 4, 6]

# 3. find index of 8
index_of_8 = original_list.index(8)
print("Index of 8:", index_of_8)

# 4. count 5
count_of_5 = original_list.count(5)
print("Count of 5:", count_of_5)
