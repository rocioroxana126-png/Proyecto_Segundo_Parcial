 (Proyecto "Tienda Online")  
 🛒 Sistema de Gestión de Ventas - Tienda Online  
 Este proyecto es una aplicación de escritorio desarrollada en Python utilizando el framework PySide6 para la interfaz gráfica.   
 El sistema permite gestionar el ciclo de vida de una venta (CRUD), incluyendo el cálculo automático de impuestos y la persistencia de datos en una base de datos SQL.  
 ⚙️ Capa de Lógica de Negocio (Servicios)
La clase VentaServicio es el componente central que maneja la lógica de control del aplicativo. Su responsabilidad principal es orquestar el flujo de datos entre la interacción del usuario y la persistencia en la base de datos.  
Funcionalidades Clave del Servicio:  
Orquestación del CRUD: Gestiona las operaciones de Crear, Leer, Actualizar y Eliminar invocando los métodos estáticos de VentaDAO  tras validar la integridad de los datos de entrada.  
Gestión de Eventos de Interfaz: Conecta las señales de los componentes de PySide6 (clics de botones, cambios en celdas) con   métodos específicos de procesamiento.  
Cálculos en Tiempo Real: Implementa el método calcular_totales_tabla, el cual reacciona a los cambios en la QTableWidget para   actualizar automáticamente el Subtotal y Total sin necesidad de refrescar la ventana.  
Validación de Reglas de Negocio:  
Controla que no existan facturas duplicadas antes de intentar una inserción.  
Asegura que los campos obligatorios (ID Cliente, Nombre, Código de Producto) contengan información válida.  
Maneja el formateo de datos, como el reemplazo de comas por puntos para asegurar la compatibilidad con tipos float de Python.  
Flujo de Datos (Workflow):  
Entrada: El usuario interactúa con la Ui_interfaz.  
Validación: El VentaServicio captura los datos, limpia espacios en blanco (strip()) y verifica tipos de datos.  
Modelado: Se instancian objetos de tipo Cliente y ProductoBase para estructurar la información.  
Persistencia: Se delega el objeto Venta resultante al VentaDAO para su almacenamiento definitivo.  
Feedback: El servicio utiliza QMessageBox para notificar al usuario el éxito o error de la operación y limpia la interfaz mediante el método limpiar().  
 🏗️ Arquitectura del Proyecto   
 El software ha sido diseñado siguiendo principios de programación orientada a objetos (POO) y una arquitectura en capas para   
 facilitar el mantenimiento:  
 Capa de Interfaz (UI): Gestionada con PySide6.   
 Implementa validaciones en tiempo real y retroalimentación mediante QMessageBox.  
 Capa de Dominio (Modelos):  
 Contiene las clases Cliente, ProductoBase y Venta, las cuales encapsulan la lógica de negocio y cálculos de subtotales/totales.  
 Capa de Datos (DAO): Implementa el patrón Data Access Object para centralizar las operaciones SQL   
 (Insertar, Actualizar, Eliminar, Buscar), separando la lógica de la base de datos de la interfaz.   
 🚀 Características Principales   
 Cálculo Automático: La aplicación calcula el Subtotal y el Total (incluyendo un IVA del 15%)  
 de forma dinámica mientras se edita latabla de productos.  
 Validaciones Robustas:   
 * Control de longitud de caracteres para códigos y nombres.Verificación de existencia previa de facturas para evitar duplicados.  
 Manejo de excepciones para formatos numéricos inválidos.Persistencia SQL:  
 Conexión eficiente para el almacenamiento físico de las transacciones.  
🛠️ Tecnologías Utilizadas  
Lenguaje:Python   
Interfaz Gráfica: PySide6 (Qt for Python)Base de Datos: SQL Server / Azure SQL (Compatible con T-SQL)Herramientas:  
Qt Designer para el diseño de interfaces (.ui).  
📋 Estructura de Clases  
Entidades de Dominio  
ProductoBase:  
Gestiona los datos del artículo, precio y unidades. Incluye propiedades decoradas con @property para el cálculo automático  
 de:$$Subtotal = Precio \times Unidades$$$$Total = Subtotal \times 1.15$$Cliente:  
Almacena la información de identificación y contacto del comprador.  
Venta: Clase integradora que relaciona un cliente con un producto para conformar una factura.  
Acceso a Datos (DAO)La clase VentaDAO centraliza las consultas:_INSERT: Registra la cabecera y el detalle en la tablaVentas.  
_SELECT: Recupera información mediante el IdFactura._UPDATE / _DELETE: Permite el mantenimiento de registros existentes.  
SE AGREGA EL LINK DEL VIDEO CON LA EJECUCION DEL PROGRAMA  

https://1drv.ms/v/c/420e760fd39caeac/IQDmYnk9Ef38SKo8wT1HKw8CAZ3XpyAh3z72q1FhAOm2DbY?e=4c8iem  

Se agrega imagenes de la estructura de las clasese y ejecucion del programa
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 171353" src="https://github.com/user-attachments/assets/3fa7455d-db2c-40cb-80d7-09f6c0e80c28" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 173348" src="https://github.com/user-attachments/assets/fb3881bf-9340-4170-b762-9ddd1290edc1" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 173535" src="https://github.com/user-attachments/assets/431441b7-eb6a-4d78-bd99-a6b6e61fd98d" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 173557" src="https://github.com/user-attachments/assets/5c220eeb-f6bf-43f9-bf03-5de72c07d6f6" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 173625" src="https://github.com/user-attachments/assets/75401678-1176-4943-a4cb-e6af60a1a6a0" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 171602" src="https://github.com/user-attachments/assets/6e7df2f3-2968-483a-926e-bae53abe8cc1" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 171639" src="https://github.com/user-attachments/assets/777c3cb9-8a9b-4e3c-8589-4b157e0aaf31" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 172311" src="https://github.com/user-attachments/assets/39fb2d51-db4e-4947-8e37-5bc884013619" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-07 172454" src="https://github.com/user-attachments/assets/13be904f-392b-4457-8b4d-717634a6e8a9" />
Nota:  
el resto de las capturas estan en el archivo pdf
