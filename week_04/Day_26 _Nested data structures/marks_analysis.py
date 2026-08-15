subjects = {
    "Python": [85, 90, 78, 92, 88],
    "Math": [70, 65, 80, 75, 85],
    "AI": [90, 95, 88, 92, 96]
}

print("--- Subject Analysis ---")
highest_avg = 0
best_subject = ""
num_students = len(subjects["Python"]) # Assuming all subjects have same number of students (5)

# 1 & 2. Average and Highest score per subject
for sub, marks in subjects.items():
    avg = sum(marks) / len(marks)
    high = max(marks)
    print(f"{sub} -> Average: {avg:.1f} | Highest: {high}")

    # 4. Track subject with highest average
    if avg > highest_avg:
        highest_avg = avg
        best_subject = sub

print(f"\n Subject with Highest Average: {best_subject} ({highest_avg:.1f})")

# 3. Overall topper (Highest total marks across all subjects)
best_student_index = 0
highest_total = 0

for i in range(num_students):
    # Calculate total marks for student at index 'i' across all subjects
    student_total = subjects["Python"][i] + subjects["Math"][i] + subjects["AI"][i]
    if student_total > highest_total:
        highest_total = student_total
        best_student_index = i

print(f" Overall Topper is Student #{best_student_index + 1} with Total Marks: {highest_total}")