# 08_dict_comprehension.py

numbers = [1, 2, 3, 4, 5]

# 1. Create a dictionary of (number: square)
# Syntax: {key: value for item in list}
squares_dict = {n: n**2 for n in numbers}

print("--- All Numbers and their Squares ---")
print(squares_dict)


# 2. Create a dictionary for EVEN numbers only
# We add an 'if' condition at the end of the comprehension
even_squares = {n: n**2 for n in numbers if n % 2 == 0}

print("\n--- Squares of EVEN numbers only ---")
print(even_squares)


# 3. Filter the first dictionary to keep only items where value > 10
# We loop through the .items() of squares_dict and filter based on 'value'
values_greater_than_10 = {k: v for k, v in squares_dict.items() if v > 10}

print("\n--- Filtered Dictionary (Values > 10) ---")
print(values_greater_than_10)