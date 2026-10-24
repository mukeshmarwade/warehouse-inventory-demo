APP_TITLE = "Warehouse Inventory"
REORDER_LEVEL = 9

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

# Call the function
show_inventory()
