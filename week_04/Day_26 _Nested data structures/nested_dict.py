# 1. Create a dictionary of dictionaries for 3 employees
employees = {
    "emp1": {"name": "Omama", "dept": "AI", "salary": 50000},
    "emp2": {"name": "Sara", "dept": "CS", "salary": 75000},
    "emp3": {"name": "Bilal", "dept": "AI", "salary": 60000}
}

# 2. Print all employees
print("--- Employee Details ---")
for emp_id, info in employees.items():
    print(f"{emp_id} -> Name: {info['name']} | Dept: {info['dept']} | Salary: Rs.{info['salary']}")

# 3. Find highest salary employee
highest_sal = 0
top_emp = ""

for emp_id, info in employees.items():
    if info['salary'] > highest_sal:
        highest_sal = info['salary']
        top_emp = info['name']

print(f"\n Highest Paid: {top_emp} (Rs.{highest_sal})")

# 4. Group by department
dept_groups = {}
for emp_id, info in employees.items():
    department = info['dept']
    name = info['name']

    # If department isn't in our new dictionary, create an empty list first
    if department not in dept_groups:
        dept_groups[department] = []

    # Append the employee name to their department list
    dept_groups[department].append(name)

print("\n--- Grouped by Department ---")
for dept, names in dept_groups.items():
    print(f"{dept}: {', '.join(names)}")