# 1. Create a dictionary where keys are departments and values are lists of students
school_depts = {
    "AI": ["Ali", "Sara", "Zaid"],
    "CS": ["Hassan", "Zara"],
    "SE": ["Bilal", "Ayesha", "Omer", "Sana"]
}

# 2. Print students of each department
print("--- Students per Department ---")
for dept, students in school_depts.items():
    # students is a list here
    student_names = ", ".join(students)
    print(f"{dept} Department: {student_names}")

    # 3. Print total students per department
print("\n--- Total Students per Department ---")
for dept, students in school_depts.items():
    print(f"{dept}: {len(students)} students")

    # 4. Search for a specific student
    search_name = "Zara"
    found = False

print("\n--- Student Search ---")
for dept, students in school_depts.items():
    if search_name in students:
        print(f" Found '{search_name}' in {dept} department.")
        found = True
        break # Stop searching once found

if not found:
    print(f" '{search_name}' not found anywhere.")