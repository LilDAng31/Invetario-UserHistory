
# =


def agregar_producto(inv, nombre, precio, cantidad):
    inv.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto agregado")


def mostrar_inventario(inv):
    if not inv:
        print("Inventario vacío")
        return

    for p in inv:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inv, nombre):
    for p in inv:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto(inv, nombre, nuevo_precio=None, nueva_cantidad=None):
    p = buscar_producto(inv, nombre)
    if p:
        if nuevo_precio is not None:
            p["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            p["cantidad"] = nueva_cantidad
        print("Producto actualizado")
    else:
        print("Producto no encontrado")


def eliminar_producto(inv, nombre):
    p = buscar_producto(inv, nombre)
    if p:
        inv.remove(p)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")


def calcular_estadisticas(inv):
    if not inv:
        return "Inventario vacío"

    unidades = sum(p["cantidad"] for p in inv)
    valor = sum(p["precio"] * p["cantidad"] for p in inv)
    mas_caro = max(inv, key=lambda x: x["precio"])
    mayor_stock = max(inv, key=lambda x: x["cantidad"])

    return {
        "unidades_totales": unidades,
        "valor_total": valor,
        "producto_mas_caro": mas_caro,
        "producto_mayor_stock": mayor_stock
    }


def fusionar_inventarios(actual, nuevos):
    for n in nuevos:
        existente = buscar_producto(actual, n["nombre"])
        if existente:
            existente["cantidad"] += n["cantidad"]
            existente["precio"] = n["precio"]
        else:
            actual.append(n)





import csv


def guardar_csv(inv, ruta):
    if not inv:
        print("Inventario vacío")
        return

    try:
        with open(ruta, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "precio", "cantidad"])

            for p in inv:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print("Archivo guardado correctamente")

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta):
    productos = []
    errores = 0

    try:
        with open(ruta, newline="") as f:
            reader = csv.reader(f)
            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Formato inválido")
                return None

            for fila in reader:
                try:
                    nombre, precio, cantidad = fila
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"Cargados: {len(productos)} | Filas inválidas: {errores}")
        return productos

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print("Error:", e)

    return None


inventario = []

ejecutando = True

while ejecutando:
    print("""
--- MENÚ ---
1. Agregar
2. Mostrar
3. Buscar
4. Actualizar
5. Eliminar
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
""")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("No encontrado")

        elif opcion == "4":
            nombre = input("Nombre: ")
            precio = input("Nuevo precio (enter para omitir): ")
            cantidad = input("Nueva cantidad (enter para omitir): ")

            actualizar_producto(
                inventario,
                nombre,
                float(precio) if precio else None,
                int(cantidad) if cantidad else None
            )

        elif opcion == "5":
            nombre = input("Nombre a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            print(stats)

        elif opcion == "7":
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos is not None:
                decision = input("¿Sobrescribir inventario? (S/N): ").upper()
                if decision == "S":
                    inventario.clear()
                    inventario.extend(nuevos)
                else:
                    fusionar_inventarios(inventario, nuevos)

        elif opcion == "9":
            print("Saliendo...")
            ejecutando = False

        else:
            print("Opción inválida")

    except Exception as e:
        print("Error:", e)





