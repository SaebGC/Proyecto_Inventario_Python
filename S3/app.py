from services import *
from files import *
inventory = [] 


def menu(): 
    while True:
        print("~" * 30)
        print("INVENTORY MENU")
        print("~" * 30)
        print("1. Add product")
        print("2. Show inventory")
        print("3. Search product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Calculate stats")
        print("7. Exit")
        print("~" * 30)

        option = input("Choose an option: ")

        # OPTION 1: ADD PRODUCT
        if option == "1":
            name = input("Enter product name: ")

            try:
                price = float(input("Enter price: "))
                amount = int(input("Enter quantity: "))

                if price < 0 or amount < 0:
                    print("Values must be positive")
                else:
                    add_product(inventory, name, price, amount)
                    print("Product added")

            except ValueError:
                print("Invalid input")

        # OPTION 2: SHOW INVENTORY
        elif option == "2":
            products = show_inventory(inventory)

            if not products:
                print("No stock available")
            else:
                for product in products:
                    print("~" * 30)
                    print(f"Name: {product['name']}")
                    print(f"Price: {product['price']}")
                    print(f"Amount: {product['amount']}")
                print("~" * 30)

        # OPTION 3: SEARCH PRODUCT
        elif option == "3":
            name = input("Product name to search: ")
            product = search_product(inventory, name)

            if product:
                print("Product found:")
                print(product)
            else:
                print("Product not found")

        # OPTION 4: UPDATE PRODUCT
        elif option == "4":
            name = input("Product name to update: ")

            try:
                new_price = float(input("New price: "))
                new_amount = int(input("New quantity: "))

                if new_price < 0 or new_amount < 0:
                    print("Values must be positive")
                else:
                    updated = update_product(inventory, name, new_price, new_amount)

                    if updated:
                        print("Product updated")
                    else:
                        print("Product not found")

            except ValueError:
                print("Invalid input")

        # OPTION 5: DELETE PRODUCT
        elif option == "5":
            name = input("Product name to delete: ")

            deleted = delete_product(inventory, name)

            if deleted:
                print("Product deleted")
            else:
                print("Product not found")

        # OPTION 6: STATS
        elif option == "6":
            stats = calculate_stats(inventory)

            if stats is None:
                print("No stock available")
            else:
                print("~" * 30)
                print(f"Total value: {stats['total_value']:.2f}$")
                print(f"Total units: {stats['total_units']}")
                print(f"Most expensive: {stats['most_expensive']['name']}")
                print(f"Highest stock: {stats['highest_stock']['name']}")
                print("~" * 30)

        # OPTION 7: EXIT
        elif option == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid option, try again")


if __name__ == "__main__":
    menu() 