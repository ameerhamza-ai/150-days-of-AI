# 1. Create an empty dictionary to store all contacts
contact_book = {}

# Start an infinite loop for the menu system
while True:
    print("\n" + "="*25)
    print(" CONTACT BOOK MENU")
    print("="*25)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Phone Number")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    # Take the user's choice
    choice = input("Enter your choice (1-6): ")

# --- ADD CONTACT ---
    if choice == '1':
        name = input("Enter contact name: ").strip()
        # Check if contact already exists
        if name in contact_book:
            print(f" Contact '{name}' already exists!")
        else:
            phone = input("Enter phone number: ").strip()
            contact_book[name] = phone
            print(f" Contact '{name}' added successfully.")

# --- SEARCH CONTACT ---
    elif choice == '2':
        name = input("Enter name to search: ").strip()
        # Check if the name is a key in the dictionary
        if name in contact_book:
            print(f" Found: {name}'s phone number is {contact_book[name]}")
        else:
            print(f" Contact '{name}' not found.")

# --- UPDATE CONTACT ---
    elif choice == '3':
        name = input("Enter name to update: ").strip()
        if name in contact_book:
            new_phone = input("Enter new phone number: ").strip()
            # Assigning a new value to an existing key overwrites (updates) it
            contact_book[name] = new_phone
            print(f" Contact '{name}' updated successfully.")
        else:
            print(f" Contact '{name}' not found.")

# --- DELETE CONTACT ---
    elif choice == '4':
        name = input("Enter name to delete: ").strip()
        if name in contact_book:
            # 'del' completely removes the key-value pair from the dictionary
            del contact_book[name]
            print(f" Contact '{name}' deleted successfully.")
        else:
            print(f" Contact '{name}' not found.")

# --- SHOW ALL CONTACTS ---
    elif choice == '5':
        # Check if dictionary is empty
        if len(contact_book) == 0:
            print(" Contact book is empty.")
        else:
            print("\n--- All Contacts ---")
            for name, phone in contact_book.items():
                print(f" Name: {name} |  Phone: {phone}")

# --- EXIT ---
    elif choice == '6':
        print(" Exiting Contact Book. Goodbye!")
        # 'break' stops the while loop entirely
        break

# --- INVALID CHOICE ---
    else:
        print(" Invalid choice! Please enter a number between 1 and 6.")