Sistema de Gestión de Inventario
Descripción del Proyecto
Este proyecto es una aplicación de línea de comandos desarrollada en Python para gestionar el inventario de una pequeña tienda.
El sistema permite registrar, actualizar, eliminar, buscar y visualizar productos en una base de datos SQLite.
Además, incluye funcionalidades avanzadas como generación de reportes de productos con bajo stock y gestión de categorías.

Funcionalidades
Gestión de Productos
Registro de Productos: Agrega nuevos productos al inventario indicando su nombre, descripción, cantidad, precio y categoría.
Actualización de Productos: Permite modificar la cantidad de productos existentes utilizando su ID.
Eliminación de Productos: Elimina productos del inventario de forma permanente.
Visualización de Productos: Muestra todos los productos del inventario con detalles como ID, nombre, descripción, cantidad, precio y categoría.
Gestión de Categorías
Visualización de Categorías: Consulta las categorías disponibles en la tienda.
Agregar Categorías: Permite incorporar nuevas categorías para productos.
Modificar Categorías: Cambia el nombre de categorías existentes.
Eliminar Categorías: Elimina categorías que ya no sean necesarias.
Búsqueda y Reportes
Búsqueda de Productos: Encuentra productos específicos por su ID, con opción a incluir búsqueda por nombre o categoría.
Reporte de Bajo Stock: Genera un informe con productos cuyo stock está por debajo de un límite especificado.
Cómo Usar la Aplicación
Instalación:

Asegúrate de tener Python 3.9 o superior instalado en tu sistema.
Descarga el archivo inventario.py y colócalo en una carpeta junto con el archivo de base de datos inventario.db (si ya existe).
Ejecución:

Abre una terminal en la carpeta donde se encuentra el archivo inventario.py.
Ejecuta el script con el comando:
python inventario.py
Menú Principal:

El sistema te presentará un menú con las siguientes opciones:
Registrar producto
Mostrar productos
Actualizar cantidad de producto
Eliminar producto
Generar reporte de bajo stock
Gestionar categorías
Salir
Interacción:

Navega por las opciones del menú escribiendo el número correspondiente y siguiendo las instrucciones en pantalla.
Requisitos del Sistema
Python 3.9 o superior
Librería estándar de Python (no se requieren instalaciones adicionales)
Estructura del Proyecto
inventario.py: Script principal que contiene toda la lógica del sistema.
inventario.db: Base de datos SQLite donde se almacenan los productos.
README.md: Documento explicativo sobre cómo usar y entender el proyecto.
Documentación Oficial de Python
Para aprender más sobre Python, visita la documentación oficial:
Python Documentation

Créditos
Este proyecto fue desarrollado por Mauricio Cox como parte del Proyecto Final Integrador (PFI) del curso de introducción a Python.

Contacto
Para consultas o sugerencias, puedes contactarme en:

Email: coxmau77@gmail.com
LinkedIn: maucox