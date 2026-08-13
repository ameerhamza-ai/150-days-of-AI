# 1. Create the initial shop inventory dictionary
inventory = {
    "apple": 50,
    "banana": 30,
    "mango": 0
}

print("--- Initial Inventory ---")
print(inventory)

# 2. Find items in stock (value > 0)
# We use dictionary comprehension to filter items with quantity greater than 0
in_stock = {item: qty for item, qty in inventory.items() if qty > 0}

print("\n--- Items IN STOCK ---")
print(in_stock)

# 3. Find out of stock items
# We just need the names of the items, so a list comprehension is perfect here
out_of_stock = [item for item, qty in inventory.items() if qty == 0]

print("\n--- OUT OF STOCK Items ---")
print(out_of_stock)

# 4. Total inventory count
# We sum up all the quantities present in the dictionary
total_items = sum(inventory.values())

print(f"\nTotal items in shop: {total_items}")

# 5. Update stock
# Let's restock mangoes, add more apples, and introduce a new item (oranges)
print("\n--- Updating Stock... ---")

# Add 20 more apples to existing stock
inventory["apple"] += 20

# Restock mangoes
inventory["mango"] = 15

# Add a completely new item that wasn't in the dict before
inventory["orange"] = 40

# Print the final updated inventory using a loop
for item, qty in inventory.items():
    # .capitalize() just makes the first letter uppercase (e.g., Apple)
    print(f"{item.capitalize()}: {qty}")