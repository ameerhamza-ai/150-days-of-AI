# 1. Tuple of tuples containing student records
students = (
    ("Ali", 85),
    ("Sara", 92),
    ("Ameer", 78)
)

names_set = set()
marks_set = set()
highest_student = ""
highest_mark = 0

# 2. Unpack each tuple inside the loop
for name, mark in students:
    # 3. Create a set of names and a set of marks
    names_set.add(name)
    marks_set.add(mark)

    # 4. Find the highest mark student
    if mark > highest_mark:
        highest_mark = mark
        highest_student = name

print(f"Names Set: {names_set}")
print(f"Marks Set: {marks_set}")
print(f"Highest Scorer: {highest_student} with {highest_mark} marks!")