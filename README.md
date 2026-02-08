  INTEGRANTES GRUPO 7  
Palma Bowen Ricardo David  
Reina Mera Roxana Rocio  
Gurumendi Chonillo Mirelli Sabrina  
Villacis Leon Nayely Valeska  
PROYECTO: "Tienda Online"    
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
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172330" src="https://github.com/user-attachments/assets/2ca04842-ce57-4912-8b89-c73d82a4c773" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172455" src="https://github.com/user-attachments/assets/c16f2284-2797-4840-bf56-d5ab220715a2" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172533" src="https://github.com/user-attachments/assets/7523f47a-e794-4dbe-be12-1ef966a37d9c" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172703" src="https://github.com/user-attachments/assets/e1a14148-bf77-4b23-939c-4e7f3b99395b" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172722" src="https://github.com/user-attachments/assets/3505b3ca-349a-4ed1-ba0a-21cb8af48839" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172739" src="https://github.com/user-attachments/assets/0332c85d-4737-465a-a1f3-3f55a583a1b2" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172801" src="https://github.com/user-attachments/assets/1fa799cb-c5cc-4970-95ed-8f80d741ef1c" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172850" src="https://github.com/user-attachments/assets/2ca28c85-f31a-4c07-9840-d17014990d98" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 172950" src="https://github.com/user-attachments/assets/19039789-00da-4cca-a128-55814e1cf798" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173033" src="https://github.com/user-attachments/assets/b883bc0b-7dd6-4e9a-94af-402b4bdd82a0" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173153" src="https://github.com/user-attachments/assets/140c6c3d-b995-455d-a23c-612b0db23bf0" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173224" src="https://github.com/user-attachments/assets/8e8ac66b-8348-45a2-b091-9cf87ca6464c" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173337" src="https://github.com/user-attachments/assets/f2b8c6ba-0b18-4f56-9150-f22633c2f31a" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173352" src="https://github.com/user-attachments/assets/a0b51314-6caa-4962-aee2-64084b1892ca" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173418" src="https://github.com/user-attachments/assets/9cb5bc8e-467a-4786-b03d-66d1d97e4cb9" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173542" src="https://github.com/user-attachments/assets/57fc4f1b-f050-4214-96cb-f64dbf4aa835" />

Se agrega capturas de estructura del proyecto con sus clases definidas

<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173750" src="https://github.com/user-attachments/assets/fddd4d8b-6571-40f8-900e-9bb8e00b1904" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173850" src="https://github.com/user-attachments/assets/f4be3a6a-a0ca-49a1-b2bc-a988c2c1d1b1" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 173930" src="https://github.com/user-attachments/assets/e835af9d-9c4c-41e0-b0e9-643fa003e168" />
<img width="1360" height="768" alt="Captura de pantalla 2026-02-08 174016" src="https://github.com/user-attachments/assets/fc038898-cd6f-48ed-9d83-4242e01c6825" />






