import sqlite3


# Crear la base de datos y la tabla si no existen
def inicializar_bd():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """
    )
    conexion.commit()
    conexion.close()


# Lista inicial de categorías disponibles
categorias = ["Tecnología", "Deportes", "Hogar", "Moda", "Juguetes"]


# Función para buscar productos
def buscar_producto():
    print("\n--- Búsqueda de Productos ---")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Categoría")
    opcion = input("Seleccione una opción: ").strip()

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    if opcion == "1":
        id_producto = input("Ingrese el ID del producto: ").strip()
        if id_producto.isdigit():
            cursor.execute("SELECT * FROM productos WHERE id = ?", (int(id_producto),))
        else:
            print("\nID no válido.\n")
            conexion.close()
            return
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ").strip()
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
    elif opcion == "3":
        # Mostrar categorías existentes
        print("\nCategorías disponibles:")
        for idx, categoria in enumerate(categorias, 1):
            print(f"{idx}. {categoria}")
        print()

        seleccion = input("Seleccione el número de la categoría: ").strip()

        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria_seleccionada = categorias[int(seleccion) - 1]
            cursor.execute(
                "SELECT * FROM productos WHERE categoria = ?", (categoria_seleccionada,)
            )
        else:
            print("\nSelección no válida.\n")
            conexion.close()
            return
    else:
        print("\nOpción no válida.\n")
        conexion.close()
        return

    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("\nNo se encontraron productos.\n")
    else:
        print("\nResultados de la búsqueda:")
        for producto in productos:
            print(
                f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]}"
            )
            print(
                f"Cantidad: {producto[3]} | Precio: ${producto[4]:.2f} | Categoría: {producto[5]}"
            )
            print("-" * 50)
        print()


# Función para gestionar las categorías
def gestionar_categorias():
    while True:
        print("\n--- Gestión de Categorías ---")
        print("1. Ver categorías")
        print("2. Agregar nueva categoría")
        print("3. Modificar una categoría")
        print("4. Eliminar una categoría")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_categorias()
        elif opcion == "2":
            agregar_categoria()
        elif opcion == "3":
            modificar_categoria()
        elif opcion == "4":
            eliminar_categoria()
        elif opcion == "5":
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")


# Mostrar las categorías actuales
def mostrar_categorias():
    print("\nCategorías disponibles:")
    for idx, categoria in enumerate(categorias, 1):
        print(f"{idx}. {categoria}")
    print()


# Agregar una nueva categoría
def agregar_categoria():
    nueva_categoria = input("Ingrese el nombre de la nueva categoría: ").strip()
    if nueva_categoria and nueva_categoria not in categorias:
        categorias.append(nueva_categoria)
        print(f"\nCategoría '{nueva_categoria}' agregada con éxito.\n")
    else:
        print("\nLa categoría ya existe o el nombre no es válido.\n")


# Modificar una categoría existente
def modificar_categoria():
    mostrar_categorias()
    indice = input("Seleccione el número de la categoría a modificar: ").strip()
    if indice.isdigit() and 1 <= int(indice) <= len(categorias):
        nueva_categoria = input("Ingrese el nuevo nombre para la categoría: ").strip()
        if nueva_categoria and nueva_categoria not in categorias:
            categorias[int(indice) - 1] = nueva_categoria
            print("\nCategoría modificada con éxito.\n")
        else:
            print("\nEl nombre ya existe o no es válido.\n")
    else:
        print("\nSelección no válida.\n")


# Eliminar una categoría
def eliminar_categoria():
    mostrar_categorias()
    indice = input("Seleccione el número de la categoría a eliminar: ").strip()
    if indice.isdigit() and 1 <= int(indice) <= len(categorias):
        categoria_eliminada = categorias.pop(int(indice) - 1)
        print(f"\nCategoría '{categoria_eliminada}' eliminada con éxito.\n")
    else:
        print("\nSelección no válida.\n")


# Registrar un producto utilizando las categorías disponibles
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    descripcion = input("Ingrese una breve descripción del producto: ").strip()
    cantidad = input("Ingrese la cantidad disponible: ").strip()
    precio = input("Ingrese el precio del producto: ").strip()

    # Validar cantidad y precio
    cantidad = int(cantidad) if cantidad.isdigit() else 0
    precio = float(precio) if precio.replace(".", "", 1).isdigit() else 0.0

    # Selección de categoría
    while True:
        print("\n--- Selección de Categoría ---")
        mostrar_categorias()
        print(f"{len(categorias) + 1}. Agregar una nueva categoría")
        seleccion = input("Seleccione una categoría por su número: ").strip()

        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria = categorias[int(seleccion) - 1]
            break
        elif seleccion == str(len(categorias) + 1):
            agregar_categoria()
        else:
            print("\nOpción no válida. Intente nuevamente.\n")

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """,
        (nombre, descripcion, cantidad, precio, categoria),
    )
    conexion.commit()
    conexion.close()

    print(
        f"\nProducto '{nombre}' registrado con éxito en la categoría '{categoria}'.\n"
    )


# Función para mostrar todos los productos
def mostrar_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("\nEl inventario está vacío.\n")
        return

    print("\nInventario actual:")
    for producto in productos:
        print(f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]}")
        print(
            f"Cantidad: {producto[3]} | Precio: ${producto[4]:.2f} | Categoría: {producto[5]}"
        )
        print("-" * 50)
    print()


# Función para actualizar la cantidad de un producto
def actualizar_producto():
    id_producto = input("Ingrese el ID del producto que desea actualizar: ").strip()
    nueva_cantidad = input("Ingrese la nueva cantidad disponible: ").strip()

    if not id_producto.isdigit() or not nueva_cantidad.isdigit():
        print("\nID o cantidad no válidos.\n")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        UPDATE productos
        SET cantidad = ?
        WHERE id = ?
    """,
        (int(nueva_cantidad), int(id_producto)),
    )
    conexion.commit()
    conexion.close()

    print(
        f"\nCantidad del producto con ID {id_producto} actualizada a {nueva_cantidad}.\n"
    )


# Función para eliminar un producto por su ID
def eliminar_producto():
    id_producto = input("Ingrese el ID del producto que desea eliminar: ").strip()

    if not id_producto.isdigit():
        print("\nID no válido.\n")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (int(id_producto),))
    conexion.commit()
    conexion.close()

    print(f"\nProducto con ID {id_producto} eliminado del inventario.\n")


# Función para generar un reporte de bajo stock
def reporte_bajo_stock():
    limite = input("Ingrese el límite de stock para el reporte: ").strip()

    if not limite.isdigit():
        print("\nLímite no válido.\n")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (int(limite),))
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print(f"\nNo hay productos con stock igual o inferior a {limite}.\n")
        return

    print(f"\nProductos con stock igual o inferior a {limite}:")
    for producto in productos:
        print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]}")
        print("-" * 50)
    print()


# Menú principal
def menu():
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar cantidad de producto")
        print("4. Eliminar producto")
        print("5. Generar reporte de bajo stock")
        print("6. Gestionar categorías")
        print("7. Buscar productos")  # Nueva opción
        print("8. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            gestionar_categorias()
        elif opcion == "7":  # Llamada a la nueva función
            buscar_producto()
        elif opcion == "8":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")


# Inicializar la base de datos y ejecutar el menú
if __name__ == "__main__":
    inicializar_bd()
    menu()
