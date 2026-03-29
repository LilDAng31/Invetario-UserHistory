# Entrada de Datos y Variables
producto= input("Ingrese el nombre del Producto: ")

# Validar precio
precio = -1
while precio <= 0:
    try:
        precio = float(input("Ingrese el precio del Prodcuto: "))
        if precio <= 0:
            print("Valor inválido. El precio debe ser mayor que 0.")
    except:
        print("Error: debes ingresar un número.")
        precio = -1

# Validar cantidad
cantidad = -1
while cantidad <= 0:
    try:
        cantidad = int(input("Ingrese la Cantidad: "))
        if cantidad <= 0:
            print("Valor inválido. La cantidad debe ser mayor que 0.")
    except:
        print("Error: debes ingresar un número entero.")
        cantidad = -1

# Calcular el total
costo_total = precio * cantidad

# Salida por consola
print("\n ---Resumen--- ")
print("Producto",producto)
print("Precio Unitario",precio)
print("Cantida",cantidad)
print("Costo total", costo_total)