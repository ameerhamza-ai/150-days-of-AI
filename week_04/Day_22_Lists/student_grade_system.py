# 1. List of students with names and marks (using tuples)
students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Zain", 78),
    ("Sana", 64),
    ("Hamza", 45)
]

# Helper function to calculate grades
def calculate_grade(marks):
    if marks >= 90: return "Grade A"
    elif marks >= 80: return "Grade B"
    elif marks >= 70: return "Grade C"
    elif marks >= 50: return "Grade D"
    else: return "Grade F"

# Initialize variables for statistics
highest_score = -1
highest_student = ""
total_marks = 0

print("--- Student Report ---")

# 2. Loop through and print each student with their grade
for name, marks in students:
    grade = calculate_grade(marks)
    print(f"{name}: {marks} — {grade}")

# 3. Logic to find the highest scorer
    if marks > highest_score:
        highest_score = marks
        highest_student = name

# Accumulate marks for class average 
total_marks += marks

print("\n--- Class Statistics ---")

 # 4. Print the highest scorer
print(f"Highest Scorer: {highest_student} with {highest_score} marks")

# 5. Calculate and print the class average
class_average = total_marks / len(students)
print(f"Class Average: {class_average:.2f}")
