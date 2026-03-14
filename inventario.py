# Bucle para validar el nombre del producto
while True:
    nombre = input("Ingresa el nombre del producto: ")
    if not nombre.isalpha():  # isalpha() verifica si todos los caracteres son letras
        print("Error, debes colocar nombres solo con letras.")
    else:
        break

print(f"Producto '{nombre}' registrado")  # Imprime el nombre del producto registrado

# Bucle para validar el precio del producto
while True:
    try:  # Intenta ejecutar el bloque de código
        precio = float(input("Ingresa precio del producto: "))  # Convierte el input a decimal
        if precio < 0:  # El precio no puede ser negativo
            print("Error, no se puede ingresar numeros negativos")
        else:
            break
    except ValueError:  # Si el usuario ingresa letras, captura el error y muestra el mensaje
        print("Error, el precio debe ser un numero decimal (Ej: 1500.50).")

print(f"Precio del producto '{nombre}' registrado: {precio:.2f}$")  # :.2f formatea a 2 decimales

# Bucle para validar la cantidad de productos
while True:
    try:  # Intenta ejecutar el bloque de código
        cantidad = int(input("Ingresa la cantidad de productos: "))  # Convierte el input a entero
        if cantidad < 0:  # La cantidad no puede ser negativa
            print("Error, agregar una cantidad positiva.")
        else:
            break
    except ValueError:  # Si el usuario ingresa letras, captura el error y muestra el mensaje
        print("Error, la cantidad debe ser un numero entero (Ej: 5).")

print(f"{cantidad} '{nombre}' registradas.\n")  # Imprime cantidad y nombre del producto

# Calcula el costo total multiplicando precio por cantidad
costo_total = precio * cantidad

print("=" * 10)
print("RESULTADOS")
print("=" * 10)
print(f"Producto: {nombre}")
print(f"Precio: {precio:.2f}$")
print(f"Cantidad: {cantidad}")
print(f"Costo total: {costo_total:.2f}$")  # :.2f formatea el total a 2 decimales
print("=" * 10) 