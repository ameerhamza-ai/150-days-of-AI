# Global list of dictionaries
students_db = []

def add_student(name, marks):
    students_db.append({"name": name, "marks": marks})
    print(f" Added: {name}")

def remove_student(name):
    # Loop through the list to find and remove the student
    for student in students_db:
        if student['name'] == name:
            students_db.remove(student)
            print(f" Removed: {name}")
            return
        print(f" {name} not found to remove.")

def find_student(name):
    for student in students_db:
        if student['name'] == name:
            print(f" Found {name} with {student['marks']} marks.")
            return
        print(f" {name} not found.")

def show_all_students():
    print("\n--- All Enrolled Students ---")
    if not students_db:
        print("Database is empty.")
        for student in students_db:
            print(f" {student['name']} - Marks: {student['marks']}")

def get_topper():
    if not students_db:
        return
    # max() using a custom lambda function to check 'marks' key
    topper = max(students_db, key=lambda s: s['marks'])
    print(f"\n TOPPER: {topper['name']} with {topper['marks']} marks!")

# Testing the functions
add_student("Ali", 85)
add_student("Sara", 92)
add_student("Hassan", 78)
show_all_students()
find_student("Sara")
remove_student("Hassan")
get_topper()