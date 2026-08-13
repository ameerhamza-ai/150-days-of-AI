marks = [45, 78, 92, 56, 88, 34, 67, 91, 73, 60]

# 1. Assign grades using an inline conditional ladder
grades = [
    "A" if m >= 90 else "B" if m >= 80 else "C" if m >= 70 else "D" if m >= 60 else "F"
    for m in marks
]

# 2. Create a Pass/Fail status list (Passing mark is 60)
status = ["Pass" if m >= 60 else "Fail" for m in marks]

# 3. Calculate average marks using list comprehension properties
average_marks = sum([m for m in marks]) / len(marks)

print("Grades:", grades)
print("Status:", status)
print("Average Marks:", average_marks)
