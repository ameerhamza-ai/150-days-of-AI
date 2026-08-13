
# 1. Create a dictionary with 5 items
student_info = {
    "name": "Ameer Hamza",
    "age": 21,
    "grade": "A",
    "subject": "Computer Science",
    "city": "Kohat"
}

# 2. Print only the keys using the .keys() method
print("--- Printing Only Keys ---")
for key in student_info.keys():
    print(key)

# Alternatively, you can just print it directly:
# print(student_info.keys())


# 3. Print only the values using the .values() method
print("\n--- Printing Only Values ---")
for value in student_info.values():
    print(value)

# Alternatively, you can just print it directly:
# print(student_info.values())


# 4. Loop through the dictionary using .items()
# 5. Print the output using f-string formatting
print("\n--- Looping using items() and f-string ---")
for key, value in student_info.items():
    print(f"Key: {key} | Value: {value}")