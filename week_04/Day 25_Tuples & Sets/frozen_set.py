# 1. Create a frozenset
# frozenset is just like a set, but you CANNOT add or remove items after creation.
normal_set = {1, 2, 3}
f_set = frozenset([1, 2, 3, 4])

print(f"Normal Set: {normal_set}")
print(f"Frozen Set: {f_set}\n")

# 2. Compare operations
normal_set.add(4)  # Works fine

try:
    # f_set.add(5) would raise AttributeError!
    print("Cannot use .add() or .remove() on frozenset!")
except AttributeError as e:
    print(e)

# 3. Set operations STILL work on frozenset!
union_set = f_set | {5, 6}
print(f"Union on frozenset works: {union_set}\n")

    # --- USE CASE EXPLANATION ---
"""
Why use frozenset?
Dictionaries in Python only accept 'immutable' keys (like strings, numbers, tuples).
A normal 'set' is mutable (changeable), so it CANNOT be a dictionary key.
A 'frozenset' is immutable, so you CAN use it as a dictionary key!
"""