class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hi! I am {self.name}, {self.age} years old, living in {self.city}.")

    def is_adult(self):
        # Returns True if age is 18 or above, else False
        return self.age >= 18

    def birthday(self):
        # Increases age by 1
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    def move_to(self, new_city):
        # Updates the city attribute
        self.city = new_city
        print(f"{self.name} has moved to {self.city}.")

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, City: {self.city})"

# --- TESTING ---
p1 = Person("Ali", 20, "Lahore")
p2 = Person("Sarah", 17, "Hangu")
p3 = Person("Hamza", 20, "Kohat")

# Test methods
p1.introduce()
print(f"Is {p2.name} an adult? {p2.is_adult()}")
p3.birthday()
p1.move_to("Multan")
print(p1)