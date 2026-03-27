"""
services.py

Contains all inventory logic:
CRUD operations and statistics.
"""


def add_product(inventory, name, price, amount):
    """
    Adds a new product to the inventory.

    Parameters:
        inventory (list): List of product dictionaries
        name (str): Product name
        price (float): Product price (>= 0)
        amount (int): Product quantity (>= 0)

    Returns:
        None
    """
    product = {
        "name": name,
        "price": price,
        "amount": amount
    }

    inventory.append(product)


def show_inventory(inventory):
    """
    Returns the full inventory list.

    Parameters:
        inventory (list): List of product dictionaries

    Returns:
        list: Inventory list
    """
    return inventory


def search_product(inventory, name):
    """
    Searches for a product by name.

    Parameters:
        inventory (list): List of product dictionaries
        name (str): Product name to search

    Returns:
        dict or None: Found product or None if not found
    """
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None


def update_product(inventory, name, new_price=None, new_amount=None):
    """
    Updates a product's price and/or quantity.

    Parameters:
        inventory (list): List of product dictionaries
        name (str): Product name to update
        new_price (float, optional): New price
        new_amount (int, optional): New quantity

    Returns:
        bool: True if updated, False if product not found
    """
    product = search_product(inventory, name)

    if product is None:
        return False

    if new_price is not None:
        product["price"] = new_price

    if new_amount is not None:
        product["amount"] = new_amount

    return True


def delete_product(inventory, name):
    """
    Deletes a product from the inventory.

    Parameters:
        inventory (list): List of product dictionaries
        name (str): Product name to delete

    Returns:
        bool: True if deleted, False if not found
    """
    product = search_product(inventory, name)

    if product is None:
        return False

    inventory.remove(product)
    return True


def calculate_stats(inventory):
    """
    Calculates inventory statistics.

    Parameters:
        inventory (list): List of product dictionaries

    Returns:
        dict or None: Dictionary with stats or None if inventory is empty
    """
    if not inventory:
        return None

    total_value = 0
    total_units = 0

    for product in inventory:
        total_value += product["price"] * product["amount"]
        total_units += product["amount"]

    most_expensive = max(inventory, key=lambda x: x["price"])
    highest_stock = max(inventory, key=lambda x: x["amount"])

    return {
        "total_value": total_value,
        "total_units": total_units,
        "most_expensive": most_expensive,
        "highest_stock": highest_stock
    }