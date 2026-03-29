#######################################
# Sistema de Invetario Basico Vesion 2#
#######################################

#Lista donde se almacena el Invetario
inventario=[]
#---Funcion para agregar al inventario
def agregar_inventario():
    nombre = input('Nombre del Producto: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantida: '))
    #---Se crea un Diciopnario con  la informacion
    producto={
    "nombre":nombre,
    "precio":precio,
    "cantidad":cantidad
   }
    #-----Se Agrega el producto al Inventario
    inventario.append(producto)
    print("Producto Agregado Correctamente.")

#---Funcion Mostrar Inventario
def mostrar_inventario():
    # Validar si la lista está vacía
    if len(inventario) == 0:
        print("El inventario está vacío ")
    else:
        print('\n***Invetario*** ')
       # Recorrer la lista con un bucle for
        for p in inventario:
         print(f'Producto: {p['nombre']} | precio: {p['precio']} | cantidad: {p['cantidad']}')

#---- FUNCIÓN: Calcular estadísticas
def calcular_estadisticas():
    # Validar si hay productos
    if len(inventario) == 0:
        print("No hay productos para calcular")
    else:
        total_valor = 0
        total_productos = 0

        # Recorrer el inventario
        for p in inventario:
            # Sumar el valor total (precio * cantidad)
            total_valor += p["precio"] * p["cantidad"]
            # Contar productos
            total_productos += p["cantidad"]

        # Mostrar resultados
        print("\n ESTADÍSTICAS")
        print(f"$ Valor total del inventario: {total_valor}")
        print(f" Cantidad total de productos: {total_productos}")

##################
# Menu Principal#
#################
op = 0

#------Bucle Principal

while op !=4:
    print("\n=== MENÚ ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular Total")
    print("4. Salir")

    try:
        op = int(input("Elige una opción: "))

        if op == 1:
            agregar_inventario()
        elif op == 2:
            if len(inventario)==0:
                print("El Invetario esta Vacio")
            else:
                mostrar_inventario()    
        elif op == 3:
            calcular_estadisticas()
        else:
            print("Opción no válida")

    except:
        print("Debes ingresar un número")


######Resumen Final########
#*RESUMEN CONCLUSIVO
#Con este programa, se puede administrar un inventario básico mediante:
# - Listas para guardar varios productos
# - Diccionarios para la representación de cada producto
# - Funciones para la organización de código
# - Ciclos (for y while) para realizar acciones de manera reiterativa y navegar por los datos
# - Condicionales para regular el flujo del programa
#
# Propósito: Aprender a crear programas sencillos utilizando Python
# Imitando un sistema de inventario real.