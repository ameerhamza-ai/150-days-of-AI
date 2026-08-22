class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.subjects = {}

    def add_subject(self, name, marks):
        self.subjects[name] = marks

    def update_marks(self, subject, new_marks):
        if subject in self.subjects:
            self.subjects[subject] = new_marks
            print(f"Updated {subject} marks to {new_marks}.")
        else:
            print("Subject not found.")

    def get_total(self):
        return sum(self.subjects.values())

    def get_average(self):
        if not self.subjects:
            return 0
        return self.get_total() / len(self.subjects)

    def get_grade(self):
        avg = self.get_average()
        calc_grade = lambda a: "A" if a >= 80 else "B" if a >= 70 else "C" if a >= 60 else "F"
        return calc_grade(avg)

    def is_passed(self):
        return self.get_average() >= 50

    def get_report(self):
        print(f"\n--- Report Card: {self.name} ({self.roll_no}) ---")
        for sub, marks in self.subjects.items():
            print(f"{sub}: {marks}")

            print("-" * 30)
            print(f"Total: {self.get_total()}")
            print(f"Average: {self.get_average():.1f}%")
            print(f"Grade: {self.get_grade()}")
            print(f"Status: {'PASSED 🎉' if self.is_passed() else 'FAILED '}")

    def __str__(self):
        return f"Student: {self.name} (Avg: {self.get_average():.1f}%)"

# --- TESTING ---
s1 = Student("Ameer", "CS-101")
s1.add_subject("Python", 85)
s1.add_subject("Math", 90)
s1.add_subject("AI", 88) 

s2 = Student("Omama", "CS-102")
s2.add_subject("Python", 40)
s2.add_subject("Math", 45)

s3 = Student("Sarah", "CS-103")
s3.add_subject("Python", 95)
s3.add_subject("Math", 92)

s1.get_report()
s2.get_report()
print(s3)