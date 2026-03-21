# Inventory Management System
### M1S2 — Control Flow and List Handling in Python

A simple command-line inventory system that lets you add products, view stock, and calculate sales statistics. Built as part of the Week 2 challenge focused on control flow structures and list/dictionary management.

---

## How to run

```bash
python main.py
```

Requires Python 3.x — no external libraries needed.

---

## Features

| Option | Description |
|--------|-------------|
| 1. Add product | Register a product with name, price, and quantity |
| 2. Show inventory | Display all registered products |
| 3. Calculate stats | Show total inventory value and total units |
| 4. Exit | Close the program |

---

## Data structure

Each product is stored as a dictionary inside a list:

```python
inventory = [
    {"name": "Pencil", "price": 500.0, "amount": 3},
    {"name": "Notebook", "price": 2000.0, "amount": 10},
]
```

---

## Input validation

- **Name** — letters only, no numbers or symbols
- **Price** — positive decimal number (e.g. `1500.50`)
- **Quantity** — positive whole number (e.g. `5`)
- **Menu option** — invalid entries show an error and re-prompt without closing the program

---

## Project structure

```
main.py       # Single file containing all logic
README.md     # This file
```

### Functions

| Function | Description |
|----------|-------------|
| `menu()` | Main loop — displays options and routes user input |
| `add_product()` | Validates and registers a new product |
| `show_inventory()` | Prints all products in the inventory |
| `calculate_stats()` | Calculates total value and total units |

---

## Concepts applied

- `if / elif / else` — menu routing and input validation
- `while` — keeps the menu running and retries invalid inputs
- `for` — iterates over the inventory to display and calculate
- `list` — stores all products
- `dict` — represents each individual product
- `try / except` — handles non-numeric inputs gracefully