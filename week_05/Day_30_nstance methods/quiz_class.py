class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []
        self.score = 0

    def add_question(self, q, options, answer):
        self.questions.append({
            "q": q,
            "options": options,
            "answer": answer
        })

    def check_answer(self, user_ans, correct_ans):
        if user_ans.strip().lower() == correct_ans.strip().lower():
            self.score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! Correct answer was: {correct_ans}\n")

    def start_quiz(self):
        print(f"=== Welcome to the {self.title} ===")
        self.score = 0 # Reset score at the start

        for index, item in enumerate(self.questions, 1):
            print(f"Q{index}: {item['q']}")
            for opt in item['options']:
                print(f"- {opt}")

            # --- MOCKING INPUT FOR TESTING ---
            user_ans = item['answer'] # Pretending user always gives the correct answer
            # ---------------------------------

            self.check_answer(user_ans, item['answer'])

    def get_result(self):
        total = len(self.questions)
        percentage = (self.score / total) * 100 if total > 0 else 0
        print(f"Final Result: {self.score}/{total} ({percentage:.1f}%)")

    def reset(self):
        self.score = 0
        print("Quiz score reset to 0.")

    def __str__(self):
        return f"Quiz: {self.title} | Questions: {len(self.questions)}"

# --- TESTING ---
q = Quiz("Python Basics Quiz")
q.add_question("What is the output of 2**3?", ["6", "8", "9"], "8")
q.add_question("Is Python compiled or interpreted?", ["Compiled", "Interpreted"], "Interpreted")
q.add_question("Keyword to define a function?", ["func", "def", "function"], "def")
q.add_question("Which bracket is used for Lists?", ["()", "{}", "[]"], "[]")
q.add_question("Can tuples be changed?", ["Yes", "No"], "No")

# start_quiz simulates the game
q.start_quiz()
q.get_result()