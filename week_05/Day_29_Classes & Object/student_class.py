class Student:
    university: str = "KUST"

    def __init__(self,name:str,age:int,gpa:float) -> None:
        self.name = name 
        self.age = age 
        self.gpa = gpa 

    def introduce(self) -> str:
        return f"Hi! I'm {self.name} from {self.university}\nMy GPA is {self.gpa}"
    def is_distinction(self) -> bool:
        return self.gpa >= 3.5

student1 = Student('Hamza',21,3.95)
print('=== Student1 Info ===')
print(student1.introduce())
print(f"Distinction Holder: {student1.is_distinction()}")

print()

student2 = Student('Sarah',20,3.5)
print('=== Student2 Info ===')
print(student2.introduce())
print(f"Distinction Holder: {student2.is_distinction()}")

print()

student3 = Student('Omama',19,3.4)
print('=== Student3 Info ===')
print(student3.introduce())
print(f"Distinction Holder: {student3.is_distinction()}")