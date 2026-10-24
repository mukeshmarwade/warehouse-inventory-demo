APP_TITLE = "Warehouse Inventory"
REORDER_LEVEL = 10

inventory = [
    {"name": "Keyboard", "stock": 5},
    {"name": "Mouse", "stock": 25},
    {"name": "Monitor", "stock": 8},
    {"name": "USB Cable", "stock": 40},
]

def show_inventory():
    print(f"\n{APP_TITLE}")
    print("-" * 30)
    for item in inventory:
        print(f"{item['name']}: {item['stock']} units")

def show_low_stock():
    print("\nLow-stock items")
    for item in inventory:
        if item["stock"] < REORDER_LEVEL:
            print(f"{item['name']}: reorder needed ({item['stock']} units)")
show_inventory()
show_low_stock()