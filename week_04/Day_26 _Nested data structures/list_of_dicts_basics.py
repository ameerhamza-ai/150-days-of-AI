# 1. Create a list of dictionaries for 4 students
students = [
    {"name": "Ali", "age": 20, "marks": 75, "city": "Lahore"},
    {"name": "Sara", "age": 22, "marks": 85, "city": "Karachi"},
    {"name": "Ameer", "age": 21, "marks": 92, "city": "Islamabad"},
    {"name": "Nida", "age": 20, "marks": 65, "city": "Lahore"}
]

# 2. Loop and print all students
print("--- All Students ---")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}, City: {student['city']}")

    # 3. Print only names
print("\n--- Student Names Only ---")
for student in students:
    print(student['name'])

    # 4. Filter students with 80+ marks
print("\n--- Top Performers (80+ Marks) ---")
for student in students:
    if student['marks'] >= 80:
        print(f"{student['name']} scored {student['marks']}")