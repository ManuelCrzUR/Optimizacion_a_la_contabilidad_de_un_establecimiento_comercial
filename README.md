# OPTIMIZACIÓN A LA CONTABILIDAD DE UN ESTABLECIMIENTO COMERCIAL

### Descripción del Proyecto:
Este es el proyecto final para el curso de programación del curso *"Programación de Computadores"* de la Universidad del Rosario, realizado por estudiantes de primer semetre del cohorte 2022-2, pertenecientes al pregrado **MACC**

**Proyecto elegido: Sistema de contabilización y administración de un establecimiento comercial**

**Integrantes del grupo:**

    - Daniel Alarcón Sanchez    
    Correo: (daniel.alarcons@urosario.ecu.co)

    - Mariana Sandoval Garzon    
    Correo: (mariana.sandovalg@urosario.edu.co)

    - Manuel Cruz Garrote   
    Correo: (manuels.cruz@urosario.edu.co)


### Tabla de Contenido

1. [Información General](#información-general)
2. [Tecnologias Usadas](#tecnologias-usadas)
3. [Instalar y Correr el Proyecto](#instalar-y-correr-el-proyecto)
4. [Como Usar el Proyecto](#como-usar-el-proyecto)
5. [FAQS](#faqs)
6. [Creditos](#creditos)
7. [Licencia](#licencia)

### Información General
## ¿De qué se encarga nuestro progama?

El programa dirigido a empresas con más de un usuario, tiene como objetivo la seguridad de la información contenida. Por ende, el funcionamiento del programa depende exclusivamente de los usuarios ya registrados. Que dependiendo del rol, pueden agregar miembros, eliminar objetos de la base de datos y acceder a un programa cajero. se puede acceder únicamente si el usuario registrado, que debe ser administrador, crea el siguiente usuario que tendrá diferentes opciones de uso dependiendo de su rol. 

El programa dirigido a empresas con más de un usuario, primero confirma que quien use el programa sea un usuario regisrado, posteriormente, dependiendo de los roles que el administrador le haya asignado, el programa, después de validar la identidad del operador, este puede acceder al menú de opciones propio de cada rol. 

El ID de los usuarios es asignado de manera aleatoria, para evitar conflictos de duplicados y aumentar la seguridad del programa en manera básica. Toda la información es almacenada en bases de datos sencillas, que se comunican con la parte lógica y con la que interactúa el usuario.

Existen los siguientes roles:

    Administrador: Es el máximo rol, tiene todas las opciones disponibles de supervisor, cajero e invitado. Además, es el único que puede crear usuarios en el programa.
    
    Supervisor: El supervisor se encarga de visualizar o editar el inventario actual. Puede imprimir facturas o usar el modo cajero.
    
    Cajero: Este rol se encarga del modo cajero (facturar a clientes, imprir la factura actual) y visualizar el inventario que se encuentre actualmente en la base de datos.
    
    Invitado: Se necesitan credenciales (Usuario y contraseña) para únicamente visualiar el inventario de la empresa.

### Tecnologias Usadas

- Git 
- Github
- Python (3.10)
- pip
- Kivy (GUI basado en Python)

### Instalar y Correr el Proyecto

Se debe tener Python 3 instalado en el computador y ejecutar el archivo llamado Ejecutable.py


### Como Usar el Proyecto
Para acceder al programa desde el comienzo, existe el usuario "ADMINISTRADOR" con la contraseña 1234, a partir de ahí se tiene acceso a los demás menús. Posteriormente, con el teclado numérico se pueden acceder a las demás opciones del programa.


### Creditos

### Licencia
MIT license