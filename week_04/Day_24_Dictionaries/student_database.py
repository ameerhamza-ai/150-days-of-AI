# 1. Create a dictionary of dictionaries (Nested Dictionary) for 3 students
students_db = {
    "Hamza": {"marks": 85, "grade": "B"},
    "Sarah": {"marks": 92, "grade": "A"},
    "Zaid": {"marks": 78, "grade": "C"}
}

# 2. Loop through the dictionary and print all details
print("--- Student Database ---")
for name, info in students_db.items():
    print(f"Name: {name} | Marks: {info['marks']} | Grade: {info['grade']}")

print("\n------------------------\n")

# 3. Find the student with the highest marks
highest_marks = 0
top_student = ""

for name, info in students_db.items():
    if info["marks"] > highest_marks:
        highest_marks = info["marks"]
        top_student = name

print(f"Student with HIGHEST marks: {top_student} ({highest_marks} marks)")

# 4. Calculate the average marks
# First, extract all the marks into a list using list comprehension
all_marks = [info["marks"] for info in students_db.values()]

# Sum the marks and divide by the total number of students
total_marks = sum(all_marks)
total_students = len(students_db)
average_marks = total_marks / total_students

print(f"Average marks of the class: {average_marks:.2f}")