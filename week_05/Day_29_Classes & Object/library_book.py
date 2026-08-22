class Book:
    def __init__(self,title,author,pages):
        self.title = title 
        self.author = author 
        self.pages = pages 
        self.is_available = True 

    def borrow(self):
        if self.is_available == True:
            self.is_available == False
            print(f"'{self.title}' borrowed successfully!")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        if self.is_available == False:
            self.is_available == True 
            print(f"'{self.title}' returned successfully!")
        else:
            print(f"'{self.title}' is already in the library.")

    def display(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"Title: {self.title} | Author: {self.author} | Pages: {self.pages} | Status: {status}")

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


print("--- Creating 3 Books ---")
b1 = Book("Atomic Habits", "James Clear", 320)
b2 = Book("Python Basics", "Hamza", 150)
b3 = Book("Deep Work", "Cal Newport", 300)

b1.display()
b2.display()

print("\n--- Borrowing and Returning ---")
b1.borrow()

b1.borrow()

b1.return_book()

print("\n--- Testing __str__ ---")
print(b1)