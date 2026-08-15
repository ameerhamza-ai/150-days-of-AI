# 1. Create a student info tuple (name, age, gpa, university)
# Tuples use parentheses ()
student_info = ("Hamza", 21, 3.8, "KUST", 21)

print(f"Original Tuple: {student_info}")

# 2. Unpack the tuple into separate variables
name, age, gpa, uni, extra_age = student_info
print(f"Unpacked: Name={name}, GPA={gpa}")

# 3. Access by index (0-based indexing)
print(f"Index 3 (University): {student_info[3]}")

# 4. Slice the tuple (get items from index 1 to 3)
sliced_tuple = student_info[1:4]
print(f"Sliced Tuple: {sliced_tuple}")

# 5. Count and Index methods
# Count how many times '21' appears in the tuple
count_21 = student_info.count(21)
# Find the first index position of '3.8'
index_gpa = student_info.index(3.8)

print(f"Count of 21: {count_21} | Index of 3.8: {index_gpa}")