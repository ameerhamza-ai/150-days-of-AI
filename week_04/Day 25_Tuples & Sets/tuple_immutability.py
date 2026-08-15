# 1. Create a tuple with 5 elements
numbers_tuple = (10, 20, 30, 40, 50)
print(f"Original Tuple: {numbers_tuple}")

# 2. Prove it is immutable using try-except
print("\n--- Trying to change a tuple item ---")
try:
    numbers_tuple[0] = 99  # This will cause an error!
except TypeError as e:
    print(f"Error caught! You cannot change a tuple: {e}")

# 3. Convert tuple to a list
numbers_list = list(numbers_tuple)
print(f"\nConverted to List: {numbers_list}")

# 4. Change the list, then convert back to tuple
numbers_list[0] = 99
new_tuple = tuple(numbers_list)

print(f"Changed and converted back to Tuple: {new_tuple}")