class TodoList:
    def __init__(self, title):
        self.title = title
        # Storing tasks as dictionaries inside a list
        self.tasks = []

    def add_task(self, task, priority="normal"):
        self.tasks.append({"task": task, "priority": priority, "status": "pending"})
        print(f"Added: '{task}'")

    def complete_task(self, task_name):
        for t in self.tasks:
            if t["task"] == task_name:
                t["status"] = "completed"
                print(f"Completed: '{task_name}'")
                return
            print(f"Task '{task_name}' not found.")

    def delete_task(self, task_name):
        for t in self.tasks:
            if t["task"] == task_name:
                self.tasks.remove(t)
                print(f"Deleted: '{task_name}'")
                return
            print(f"Task not found.")

    def show_pending(self):
        print(f"\n--- Pending Tasks in {self.title} ---")
        for t in self.tasks:
            if t["status"] == "pending":
                print(f"- {t['task']} (Priority: {t['priority']})")

    def show_completed(self):
        print(f"\n--- Completed Tasks ---")
        for t in self.tasks:
            if t["status"] == "completed":
                print(f"- {t['task']}")

    def show_all(self):
        print(f"\n--- All Tasks in {self.title} ---")
        for t in self.tasks:
            print(f"[{t['status'].upper()}] {t['task']}")

    def clear_completed(self):
        # Re-build list keeping only pending tasks
        self.tasks = [t for t in self.tasks if t["status"] == "pending"]
        print("\nCleared all completed tasks.")

    def __str__(self):
        total = len(self.tasks)
        pending = sum(1 for t in self.tasks if t["status"] == "pending")
        return f"TodoList: {self.title} | Total Tasks: {total} | Pending: {pending}"

# --- TESTING ---
my_list = TodoList("My Python Goals")
my_list.add_task("Learn OOP", "high")
my_list.add_task("Build a project")
my_list.add_task("Read documentation", "low")

my_list.complete_task("Learn OOP")
my_list.show_pending()
my_list.clear_completed()
print(my_list)