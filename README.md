<<<<<<< HEAD
# MiniCore MVT

# Objetivo
Presentar las funcionalidades del proyecto Core MVC, en base a lo planteado en el documento de análisis aprobado.

# Sobre el Proyecto
### Descripción
- Como primer instancia, se creó el proyecto enfocado para su respectiva implementación en un negocio real llamado "El Rincón del Sabor",
  que corresponde a una heladería ubicada en la ciudad de Quito, en el sector de Las Casas.
- Para esta fase final del proyecto se implementaron las funcionalidades de los módulos de "Rentabilidad" y "Costo-Eficiencia".
=======
# MejoresPracticas_CoreMVC

# Objetivo
En base al taller formativo, aplicar al menos 2 principios solid y 2 patrones de diseño en el Core MVC.

# Sobre el Proyecto
### Descripción
- El proyecto está enfocado para su respectiva implementación en un negocio real llamado "El Rincón del Sabor",
  que corresponde a una heladería ubicada en la ciudad de Quito, en el sector de Las Casas.
- Se han implementado las funcionalidades de los módulos de "Rentabilidad", "Costo-Eficiencia" y "Pedidos".
>>>>>>> 99225e61391172fa5b901f547ca69b6c1dfffc55
- Igualmente se permite crear nuevos usuarios así como su logueo respectivo para ingresar a las funcionalidades de CRUD y del MiniCore como tal.
- Además, cabe recalcar que se implementó un método de cifrado como alternativa de seguridad dentro de la información que se ingresa al momento de crear una nueva cuenta.
- Así también, se insertó un control para que usuarios no identificados o "no logueados" no tengan la capacidad de ingresar dentro de los otros módulos de la página.
- Finalmente, es importante recalcar que se han realizado verificaciones de campos vacíos y controles en las contraseñas para que exista un mayor control.
  
### Framework empleado:
- Se utiliza Django como framework para el desarrollo web.

### MiniCore del Proyecto:
- El MiniCore del sistema está enfocado en clasificar los productos en categorías (dependiendo del tipo de producto). Para cada categoría se calculará el costo promedio de los productos y se lo comparará con el precio de venta promedio, por lo tanto, esto permitirá determinar qué categoría de producto es más rentable.
- Además, el MiniCore también brindará la posibilidad de ponderar el costo de los insumos suministrados por los proveedores y el tiempo promedio que tardan en despacharlos o entregarlos. De esta manera, se puede analizar cuál de ellos ofrece la mejor relación costo-eficiencia.
<<<<<<< HEAD

# Vista de la Página Principal:
![Imagen](https://raw.githubusercontent.com/DeividN21/Tarea5_AdminMVC/ff857f86d70cd6f3f4bc5d14c86a51cec5d63a87/Captura%20de%20pantalla%202024-11-07%20084014.png)

# Instrucciones para Navegar por la Página
### Primero:
- Si es un usuario nuevo tiene la posibilidad de registrar una cuenta.
- Si ya cuenta con un registro previo, para ingresar a los otros módulos se requiere las respectivas credenciales.

### Segundo:
- Una vez logueado, el usuario puede ingresar a los otros módulos que corresponden a las funcionalidades CRUD y los módulos relacionados con el MiniCore propuesto.

### Tercero:
- Si el usuario quiere salir puede aplastar el botón de "Cerrar Sesión", el cual redirige a la página web principal.

# Enlace del Video de Demostración
- enlace
  
=======
- Y adicional, el MiniCore tiene la funcionalidad de calcular entre un rango de fechas los proveedores que han entregado más rápido cierto tipo de producto.

# Patrones de Diseño Aplicados
### Patrón Creacional: Singleton
- Patrón que permite asegurar de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.
- Dentro del proyecto se ha implementado el patrón en: "login_views.py" / Con el objetivo de manejar los mensajes de error de manera única.
  
![Imagen](https://raw.githubusercontent.com/DeividN21/Tarea5_AdminMVC/ff857f86d70cd6f3f4bc5d14c86a51cec5d63a87/Captura%20de%20pantalla%202024-11-07%20084014.png)

### Patrón Creacional: Builder
- Patrón que permite construir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
- Dentro del proyecto se ha implementado el patrón en: "proveedor_views.py" / Con la finalidad de crear objetos de tipo Proveedor.

![Imagen](https://raw.githubusercontent.com/DeividN21/Tarea5_AdminMVC/ff857f86d70cd6f3f4bc5d14c86a51cec5d63a87/Captura%20de%20pantalla%202024-11-07%20084014.png)

# Principios SOLID Aplicados
### Principio: Principio de Responsabilidad Única (SRP)
- El principio SRP establece que una clase o función debe tener una única responsabilidad.
- Dentro del proyecto se ha implementado el principio en: "pedidos_views.py" / Con el objetivo de separar la lógica de filtrado y cálculo de proveedores más rápidos.

![Imagen](https://raw.githubusercontent.com/DeividN21/Tarea5_AdminMVC/ff857f86d70cd6f3f4bc5d14c86a51cec5d63a87/Captura%20de%20pantalla%202024-11-07%20084014.png)

### Principio: Principio de Código Abierto/Cerrado (OCP)
- El principio OCP establece que las entidades de software deben estar abiertas para la extensión pero cerradas para la modificación.
- Dentro del proyecto se ha implementado el principio en: "producto_views.py" / Con la finalidad de permitir la extensión de la lógica de guardado sin modificar la función existente.

![Imagen](https://raw.githubusercontent.com/DeividN21/Tarea5_AdminMVC/ff857f86d70cd6f3f4bc5d14c86a51cec5d63a87/Captura%20de%20pantalla%202024-11-07%20084014.png)

# Enlace del Video de Demostración
- enlace

>>>>>>> 99225e61391172fa5b901f547ca69b6c1dfffc55
# Enlace con el deploy
- enlace
