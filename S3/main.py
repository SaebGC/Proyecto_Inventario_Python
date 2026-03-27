#This is the M1S3 inventory 


inventory = []

def menu():
    """
    Displays the main menu in a loop until the user chooses to exit.
    Uses a while loop to keep the program running and if/elif/else
    to route each option to the correct function.
    """
    while True:  
        print("~"*23)
        print("MENU INVENTORY")
        print("~"*23)
        print("1.Add product")
        print("2.Show inventory")
        print("3.Search product")
        print("4.Update product")
        print("5.Delete product")
        print("6.Calculate stats")
        print("7.Exit")
        print("~"*23)

        option = input("Choose an option:1.Add product, 2.Show inventory, 3.Search product, 4.Update product, 5.Delete product, 6.Calculate stats, 7.Exit ").lower()

        # Route to the correct function based on user input

        if option == "1":
            add_product()
        
        elif option == "2":
            show_inventory()

        elif option == "3":
            name = input("Product name to search: ")
            product = search_product(name)
            if product:
                print(f"Product found: {product}")
            else:
                print("Product not found")
        
        elif option == "4":
            update_product()
        
        elif option == "5":
            delete_product()
        
        elif option == "6":
            calculate_stats()
        
        elif option == "7":
        # Exit the loop and end the program
            print("Leaving the program")
            break

        else: 
        # Handle any invalid input without closing the program

            print("Error. Try again" )

def add_product():
    """
    Asks the user for product details and adds it to the inventory.
    Validates each field:
      - Name: letters only (isalpha)
      - Price: positive decimal number (float)
      - Quantity: positive whole number (int)
    Each product is stored as a dictionary inside the inventory list.
    """
    while True:
        name = input("Type the product name: ")
        if not name.isalpha():  # isalpha() verifica si todos los caracteres son letras
            print("Error, you must enter names with only letters.")
        else:
            break

    while True:
        try:  # Intenta ejecutar el bloque de código
            price = float(input("Type the product price: "))  # Convierte el input a decimal
            if price < 0:  # El precio no puede ser negativo
                print("Error, negative numbers cannot be entered.")
            else:
                break
        except ValueError:  # Si el usuario ingresa letras, captura el error y muestra el mensaje
            print("Error, the price must be a decimal number(Like: 1500.50).")
            
    while True:
        try:  # Intenta ejecutar el bloque de código
            amount = int(input("Enter the quantity of products: "))  # Convierte el input a entero
            if amount < 0:  # La cantidad no puede ser negativa
                print("Error, add a positive amount.")
            else:
                break
        except ValueError:  # Si el usuario ingresa letras, captura el error y muestra el mensaje
            print("Error, the quantity must be a whole number (like: 5).")  

         # Build the product dictionary and append it to the inventory list   
    product = {
        "name": name,
        "price":price,
        "amount": amount 
    }

    inventory.append(product)
    print("The product was added")

def show_inventory():
    
    """
    Displays all products currently in the inventory.
    Uses a for loop to iterate over each product dictionary.
    If the inventory is empty, shows a message instead.
    """
    
    # Check if there are no products registered yet

    if not inventory:
        print("No stock available")
        return
    
    print("Inventory list:")
    for products in inventory:
        print("~"*23)
        print(f"Name: {products['name']}")
        print(f"Price: {products['price']}")
        print(f"Amount: {products['amount']}")
        print(f"~"*23)

def search_product(name):
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None

def update_product():
    name = input("Product name to update: ")
    product = search_product(name)

    if product is None:
        print("Product not found")
        return

while True:
    try:  # Intenta ejecutar el bloque de código
        new_price = float(input("New price: "))  # Convierte el input a decimal
        if new_price < 0:
            print("Error, negative numbers cannot be entered.")
        else:
            break
    except:
        print("Error, the price must be a decimal number (Like: 1500.50).")
    
while True:
    try:  # Intenta ejecutar el bloque de código
        new_amount = int(input("New quantity: "))  # Convierte el input a entero
        if new_amount < 0:
            print("Error, add a positive amount.")
        else:
            break
    except:
        print("Error, the quantity must be a whole number (like: 5).")


product["price"] = new_price
product["amount"] = new_amount

print("Product updated")

def delete_product():
    name = input("Product name to delete: ")
    product = search_product(name)

    if product is None:
        print("Product not found")
        return

    inventory.remove(product)
    print("Product deleted")

def calculate_stats():
    """
    Calculates and displays two statistics from the inventory:
      - Total inventory value: sum of (price x quantity) for all products.
      - Total units registered: sum of all quantities.
    Uses a for loop to accumulate the values.
    """

     # Cannot calculate stats if there are no products

    if not inventory:
        print("No stock available")
        return
    
    total_value = 0
    total_units = 0

    for product in inventory:
        total_value += product['price'] * product['amount']
        total_units += product['amount'] 

    most_expensive = max(inventory, key=lambda x: x["price"])    
    highest_stock = max(inventory, key=lambda x: x["amount"])

    # Those are the results 

    print("~"*23)
    print(f"Total inventory value: {total_value:.2f}$")
    print(f"Total units: {total_units}")
    print(f"Most expensive product: {most_expensive['name']}")
    print(f"Highest stock product: {highest_stock['name']}")
    print("")
    print("~"*23) 

if __name__ == "__main__": 
    menu()  # Start the program by calling the menu function when the script is run directly
