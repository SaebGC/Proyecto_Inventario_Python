inventory = []

def menu():
    while True: 
        print("~"*23)
        print("MENU INVENTORY")
        print("~"*23)
        print("1.Add product")
        print("2.Show inventory")
        print("3.Calculate stats")
        print("4.Exit")
        print("~"*23)

        option = input("Choose an option:1.Add product, 2.Show inventory, 3.Calculate stats, 4.Exit ").lower()

        if option == "1":
            add_product()
        
        elif option == "2":
            show_inventory()

        elif option == "3":
            calculate_stats()
        
        elif option == "4" or "Exit":
            print("Leaving the program")
            break

        else: 
            print("Error. Try again" )

def add_product():

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
            
    product = {
        "name": name,
        "price":price,
        "amount": amount,
    }

    inventory.append(product)
    print("The product was added")

def show_inventory():

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

def calculate_stats():

    if not inventory:
        print("No stock available")
        return
    
    cumulative_total = 0
    total_units = 0

    for products in inventory:
        price = products['price']
        amount = products['amount']

        cumulative_total += price * amount
        total_units += amount

    print("~"*23)
    print(f"Total inventory value: {cumulative_total:.2f}$")
    print(f"Registered products: {total_units}")
    print("")
    print("~"*23)

if __name__ == "__main__":
    menu()

        