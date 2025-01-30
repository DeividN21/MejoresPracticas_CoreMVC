![image](https://github.com/user-attachments/assets/88219c8c-d3c6-4bcb-900f-7cee12e492d3)# MejoresPracticas_CoreMVC

# Objetivo
En base al taller formativo, aplicar al menos 2 principios solid y 2 patrones de diseño en el Core MVC.

# Sobre el Proyecto
### Descripción
- El proyecto está enfocado para su respectiva implementación en un negocio real llamado "El Rincón del Sabor",
  que corresponde a una heladería ubicada en la ciudad de Quito, en el sector de Las Casas.
- Se han implementado las funcionalidades de los módulos de "Rentabilidad", "Costo-Eficiencia" y "Pedidos".
- Igualmente se permite crear nuevos usuarios así como su logueo respectivo para ingresar a las funcionalidades de CRUD y del MiniCore como tal.
- Además, cabe recalcar que se implementó un método de cifrado como alternativa de seguridad dentro de la información que se ingresa al momento de crear una nueva cuenta.
- Así también, se insertó un control para que usuarios no identificados o "no logueados" no tengan la capacidad de ingresar dentro de los otros módulos de la página.
- Finalmente, es importante recalcar que se han realizado verificaciones de campos vacíos y controles en las contraseñas para que exista un mayor control.
  
### Framework empleado:
- Se utiliza Django como framework para el desarrollo web.

### MiniCore del Proyecto:
- El MiniCore del sistema está enfocado en clasificar los productos en categorías (dependiendo del tipo de producto). Para cada categoría se calculará el costo promedio de los productos y se lo comparará con el precio de venta promedio, por lo tanto, esto permitirá determinar qué categoría de producto es más rentable.
- Además, el MiniCore también brindará la posibilidad de ponderar el costo de los insumos suministrados por los proveedores y el tiempo promedio que tardan en despacharlos o entregarlos. De esta manera, se puede analizar cuál de ellos ofrece la mejor relación costo-eficiencia.
- Y adicional, el MiniCore tiene la funcionalidad de calcular entre un rango de fechas los proveedores que han entregado más rápido cierto tipo de producto.

# Patrones de Diseño Aplicados
### Patrón Creacional: Singleton
- Patrón que permite asegurar de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.
- Dentro del proyecto se ha implementado el patrón en: "login_views.py" / Con el objetivo de manejar los mensajes de error de manera única.
  
![Imagen](https://raw.githubusercontent.com/DeividN21/MejoresPracticas_CoreMVC/d8eab4f323188ae9777f1544f47740ab3fafeb94/Singleton.png)

### Patrón Creacional: Builder
- Patrón que permite construir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
- Dentro del proyecto se ha implementado el patrón en: "proveedor_views.py" / Con la finalidad de crear objetos de tipo Proveedor.

![Imagen](https://raw.githubusercontent.com/DeividN21/MejoresPracticas_CoreMVC/d8eab4f323188ae9777f1544f47740ab3fafeb94/Builder.png)

# Principios SOLID Aplicados
### Principio: Principio de Responsabilidad Única (SRP)
- El principio SRP establece que una clase o función debe tener una única responsabilidad.
- Dentro del proyecto se ha implementado el principio en: "pedidos_views.py" / Con el objetivo de separar la lógica de filtrado y cálculo de proveedores más rápidos.

![Imagen](https://raw.githubusercontent.com/DeividN21/MejoresPracticas_CoreMVC/d8eab4f323188ae9777f1544f47740ab3fafeb94/SRP.png)

### Principio: Principio de Código Abierto/Cerrado (OCP)
- El principio OCP establece que las entidades de software deben estar abiertas para la extensión pero cerradas para la modificación.
- Dentro del proyecto se ha implementado el principio en: "producto_views.py" / Con la finalidad de permitir la extensión de la lógica de guardado sin modificar la función existente.

![Imagen](https://raw.githubusercontent.com/DeividN21/MejoresPracticas_CoreMVC/d8eab4f323188ae9777f1544f47740ab3fafeb94/OCP.png)

# Enlace del Video de Demostración
- https://youtu.be/QX69JEabUhQ

# Enlace con el deploy
- https://mejorespracticas-coremvc.onrender.com
