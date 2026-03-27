import csv
from services import search_product  # Para poder usar search_product al fusionar

def save_csv(inventory, path):
    if not inventory:
        print("Inventory is empty. Nothing to save.")
        return
    try:
        with open(path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "price", "amount"])
            writer.writeheader()
            writer.writerows(inventory)
        print(f"Inventory saved to {path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_csv(inventory, path):
    try:
        with open(path, "r", newline="") as file:
            reader = csv.DictReader(file)
            loaded = []
            errors = 0
            for row in reader:
                try:
                    name = row["name"]
                    price = float(row["price"])
                    amount = int(row["amount"])
                    if price < 0 or amount < 0:
                        errors += 1
                        continue
                    loaded.append({"name": name, "price": price, "amount": amount})
                except:
                    errors += 1
        # Ask user overwrite or merge
        choice = input("Overwrite current inventory? (Y/N): ").strip().upper()
        if choice == "Y":
            inventory.clear()
            inventory.extend(loaded)
            print(f"Inventory overwritten. {len(loaded)} products loaded. {errors} rows skipped.")
        else:
            # Merge
            for item in loaded:
                existing = search_product(inventory, item["name"])
                if existing:
                    existing["amount"] += item["amount"]
                    existing["price"] = item["price"]
                else:
                    inventory.append(item)
            print(f"Inventory merged. {len(loaded)} products loaded. {errors} rows skipped.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading file: {e}")