# Cart is a list of dictionaries
cart = [
    {"item": "Apple", "price": 100, "qty": 2},
    {"item": "Banana", "price": 50, "qty": 6}
]

# 1. Add item to cart
cart.append({"item": "Mango", "price": 150, "qty": 3})
print(" Item added to cart.")

# 2. Update quantity (e.g., Update Banana qty to 10)
for product in cart:
    if product["item"] == "Banana":
        product["qty"] = 10
        print(" Updated Banana quantity to 10.")

# 3. Remove an item (e.g., Apple)
for product in cart:
    if product["item"] == "Apple":
        cart.remove(product)
        print(" Removed Apple from cart.")
        break # Exit loop after removing

# 4. Calculate total bill
total_bill = 0
print("\n--- Final Receipt ---")
for product in cart:
    item_total = product["price"] * product["qty"]
    total_bill += item_total
    print(f"{product['item']}: Rs.{product['price']} x {product['qty']} = Rs.{item_total}")

print(f"Total Amount: Rs.{total_bill}")

# 5. Apply 10% discount
discount = total_bill * 0.10
payable = total_bill - discount
print(f"Discount (10%): -Rs.{discount}")
print(f" Payable Amount: Rs.{payable}")