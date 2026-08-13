names = ["Ali", "Sara", "Ameer", "Zara", "Hassan"]
marks = [85, 92, 78, 95, 88]

# 1. Zip lists together to create the student marks dictionary
students_dict = {names[i]: marks[i] for i in range(len(names))}

# 2. Filter the dictionary to get students with 90+ marks
top_students = {name: mark for name, mark in students_dict.items() if mark >= 90}

print("All Students:", students_dict)
print("90+ Students:", top_students)
