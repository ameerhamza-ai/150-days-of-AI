class Inventory:
    def __init__(self, store_name):
        self.store_name = store_name
        # Dictionary structure: {item_name: {"price": x, "qty": y}}
        self.items = {}

    def add_item(self, name, price, qty):
        self.items[name] = {"price": price, "qty": qty}
        print(f"Added {name} (Qty: {qty})")

    def sell_item(self, name, qty):
        if name in self.items and self.items[name]["qty"] >= qty:
            self.items[name]["qty"] -= qty
            print(f"Sold {qty} of {name}")
        else:
            print(f"Cannot sell {qty} {name}. Out of stock or missing.")

    def restock(self, name, qty):
        if name in self.items:
            self.items[name]["qty"] += qty
            print(f"Restocked {name}. New Qty: {self.items[name]['qty']}")
        else:
            print("Item does not exist. Use add_item first.")

    def get_total_value(self):
        total = sum(item["price"] * item["qty"] for item in self.items.values())
        return total

    def low_stock(self, threshold=5):
        print(f"\n--- Low Stock Alert (<{threshold}) ---")
        for name, data in self.items.items():
            if data["qty"] < threshold:
                print(f"- {name} (Only {data['qty']} left)")

    def display_inventory(self):
        print(f"\n--- {self.store_name} Inventory ---")
        for name, data in self.items.items():
            print(f"{name} | Price: Rs.{data['price']} | Qty: {data['qty']}")

    def __str__(self):
        return f"Store: {self.store_name} | Total Unique Items: {len(self.items)} | Total Value: Rs.{self.get_total_value()}"

# --- TESTING ---
store = Inventory("Hamza's Tech Store")
store.add_item("Laptop", 50000, 10)
store.add_item("Mouse", 500, 4)
store.add_item("Keyboard", 1500, 20)

store.sell_item("Laptop", 2)
store.sell_item("Mouse", 3)
store.restock("Mouse", 10)

store.low_stock()
store.display_inventory()
print(store)