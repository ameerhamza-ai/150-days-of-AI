class_a = {"Ali", "Sara", "Ameer", "Zara", "Hassan"}
class_b = {"Sara", "Ameer", "Bilal", "Nida", "Hassan"}

# 1. Union (|): Total unique students in both classes
total_students = class_a | class_b
print(f"Union (Total Students): {total_students}\n")

# 2. Intersection (&): Students present in BOTH classes (Common)
common_students = class_a & class_b
print(f"Intersection (Common Students): {common_students}\n")

# 3. Difference (-): Students ONLY in class_a (not in class_b)
only_in_a = class_a - class_b
print(f"Difference (Only in Class A): {only_in_a}\n")

# 4. Symmetric Difference (^): Students in A or B, but NOT in both
unique_to_each = class_a ^ class_b
print(f"Symmetric Difference (Not in both): {unique_to_each}")