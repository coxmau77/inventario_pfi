# **Sistema de Gestión de Inventario**

<a href="https://github.com/coxmau77/inventario_pfi" target="_blank" rel="noopener noreferrer">Repositorio en [gitHub]</a>

### **Descripción del Proyecto**

Este proyecto es una aplicación de línea de comandos desarrollada en **Python** para gestionar el inventario de una pequeña tienda.  
El sistema permite registrar, actualizar, eliminar, buscar y visualizar productos en una base de datos SQLite.  
Además, incluye funcionalidades avanzadas como generación de reportes de productos con bajo stock y gestión de categorías.

![Descripcion del proyecto](./img/Captura%20de%20pantalla%202024-12-17%20143642.png)
![Código](./img/Captura%20de%20pantalla%202024-12-17%20131431.png)

---

## **Funcionalidades**

### **Gestión de Productos**

- **Registro de Productos:** Agrega nuevos productos al inventario indicando su nombre, descripción, cantidad, precio y categoría.

![Registro de Productos](./img/Captura%20de%20pantalla%202024-12-17%20151154.png)

- **Visualización de Productos:** Muestra todos los productos del inventario con detalles como ID, nombre, descripción, cantidad, precio y categoría.

![Visualización de Productos](./img/Captura%20de%20pantalla%202024-12-17%20151725.png)

- **Actualización de Productos:** Permite modificar la cantidad de productos existentes utilizando su ID.

![Actualización de Productos](./img/Captura%20de%20pantalla%202024-12-17%20152154.png)

- **Eliminación de Productos:** Elimina productos del inventario de forma permanente.

![Eliminación de Productos](./img/Captura%20de%20pantalla%202024-12-17%20152646.png)

### **Gestión de Categorías**

- **Visualización de Categorías:** Consulta las categorías disponibles en la tienda.

![Visualización de Categorías](./img/Captura%20de%20pantalla%202024-12-17%20163557.png)

- **Agregar Categorías:** Permite incorporar nuevas categorías para productos.

![Agregar Categorías](./img/Captura%20de%20pantalla%202024-12-17%20163843.png)


- **Modificar Categorías:** Cambia el nombre de categorías existentes.

![Modificar Categorías](./img/Captura%20de%20pantalla%202024-12-17%20164244.png)

- **Eliminar Categorías:** Elimina categorías que ya no sean necesarias.

![Modificar Categorías](./img/Captura%20de%20pantalla%202024-12-17%20164516.png)

### **Búsqueda y Reportes**

- **Búsqueda de Productos:** Encuentra productos específicos por su ID, con opción a incluir búsqueda por nombre o categoría.

![Búsqueda de Productos](./img/Captura%20de%20pantalla%202024-12-17%20172457.png)

- **Reporte de Bajo Stock:** Genera un informe con productos cuyo stock está por debajo de un límite especificado.

![Reporte de Bajo Stock](./img/Captura%20de%20pantalla%202024-12-17%20165046.png)

---

## **Cómo Usar la Aplicación**

1. **Instalación:**

   - Asegúrate de tener **Python 3.9** o superior instalado en tu sistema.
   - Descarga el archivo `inventario.py` y colócalo en una carpeta junto con el archivo de base de datos `inventario.db` (si ya existe).

2. **Ejecución:**

   - Abre una terminal en la carpeta donde se encuentra el archivo `inventario.py`.
   - Ejecuta el script con el comando:
     ```bash
     python inventario.py
     ```

3. **Menú Principal:**

   - El sistema te presentará un menú con las siguientes opciones:
     - Registrar producto
     - Mostrar productos
     - Actualizar cantidad de producto
     - Eliminar producto
     - Generar reporte de bajo stock
     - Gestionar categorías
     - Salir

![Menú Principal](./img/Captura%20de%20pantalla%202024-12-17%20165750.png)

4. **Interacción:**
   - Navega por las opciones del menú escribiendo el número correspondiente y siguiendo las instrucciones en pantalla.

---

## **Requisitos del Sistema**

- **Python 3.9 o superior**
- Librería estándar de Python (no se requieren instalaciones adicionales)

---

## **Estructura del Proyecto**

- **`inventario.py`**: Script principal que contiene toda la lógica del sistema.
- **`inventario.db`**: Base de datos SQLite donde se almacenan los productos.
- **`README.md`**: Documento explicativo sobre cómo usar y entender el proyecto.

---

## **Documentación Oficial de Python**

Para aprender más sobre Python, visita la documentación oficial:  
[Python Documentation](https://docs.python.org/3/)

---

### **Créditos**

Este proyecto fue desarrollado por **Mauricio Cox** como parte del Proyecto Final Integrador (PFI) del curso de introducción a Python mediante la Agencia de Habilidades para el futuro del Ministerio de Educación y Talento Tech 2024.

---

### **Contacto**

Para consultas o sugerencias, puedes contactarme en:

- **Email:** coxmau77@gmail.com
- **LinkedIn:** [maucox](https://www.linkedin.com/in/coxmau77/)
