library = {
    "Python": ["Crash Course", "Fluent Python"],
    "AI": ["Deep Learning", "AI: A Modern Approach"],
    "Math": ["Calculus", "Linear Algebra"]
}

# 1. Search books by category
category_to_search = "Python"
if category_to_search in library:
    print(f" {category_to_search} Books: {library[category_to_search]}")

# 2. Add a new book to a category
new_book = "Automate the Boring Stuff"
category = "Python"
# Since library[category] is a list, we can just use .append()
library[category].append(new_book)
print(f"\n Added '{new_book}' to {category}.")

# 3. Remove a book
book_to_remove = "Calculus"
category_remove = "Math"
if book_to_remove in library[category_remove]:
    library[category_remove].remove(book_to_remove)
    print(f" Removed '{book_to_remove}' from {category_remove}.")

# 4. Total books count
# We sum the lengths of all lists in the dictionary
total_books = sum(len(books) for books in library.values())
print(f"\n Total books in library: {total_books}")

print("\n--- Updated Library ---")
for cat, books in library.items():
    print(f"{cat}: {len(books)} books -> {books}")