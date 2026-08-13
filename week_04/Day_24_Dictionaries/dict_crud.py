# 1. Create a student dictionary
student = {"name":"Ameer Hamza","age":20,"course":"Artificial Intelligence"}
print("Original Dictionary:", student)

# 2. Access using .get()
# If key exists, it returns the value
student_name = student.get("name")
print("Access Name:", student_name)

# 3. Use a default value with .get()
# If key does not exist, it returns the fallback value instead of raising an error
student_gpa = student.get("gpa",0.0)
print("Access GPA (with default):", student_gpa)

# 4. Perform multiple updates using .update()
student.update({"age":21,"university":"KUST","department":"IoC"})
print("After Multiple Updates:", student)

# 5. Remove an item using .pop()
# Removes the specified key and returns its value

removed_course = student.pop("course")
print("Removed Course:", removed_course)
print("Final Dictionary:", student)