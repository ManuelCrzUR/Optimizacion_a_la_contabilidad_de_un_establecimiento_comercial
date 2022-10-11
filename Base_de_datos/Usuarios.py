"""Módulo Usuarios

    Este módulo se encarga de crear objetos con la clase usuarios y ejecutar algunos metodos a estos mismos.
    
    Los metodos que estan en la clase Usuario son:
        __init__
        __str__
        AñadirSalario
        AumentarSalario
        DisminuirSalario
        Promover
        CambiarContraseña
        
    Si desea comprobar su funcionamiento, puede visitar el módulo U_prueba_Usuarios
"""

class Usuario:
    """Representa un Usuario
    
    Atributos:
        nombre (str): [Nombre]
        rol (str): [rol]
        usuario (str): [Usuario]
        contraseña (str): [Contraseña]
        id (str): [id]
        salario (int)"""
        
    def __init__(self, Nombre: str, rol: str, Usuario: str, Contraseña: str, id: str, salario: int = 0):
        """Inicializa en objeto de tipo Usuario

        Args:
            Nombre (str): Distinguidor de objeto, personal
            rol (str): Papel que este cumple en la organización
            Usuario (str): Identificador del objeto Usuario.
            Contraseña (str): Comprobador de pertenencia al Usuario.
            id (str): Identificador en al organización, da acceso a ciertas funciones.
            salario (int, opcional): Valor de remuneracion mensual. Por defecto None
        """
        self.rol = rol.upper()
        self.nombre = Nombre
        self.salario = salario
        self.id = id
        self.usuario = Usuario
        self.contraseña = Contraseña
            
        if self.rol != None:
            self.rol.upper()
            
   
    def __str__(self) -> str:
        """Resume el objeto tipo usuario con los datos no confidenciales

        Returns:
            str: Mensaje con el rol, nombre, id, usuario y salarios del objeto de la clase Usuario
        """

        if self.salario == None:
            salario = "No cuenta con salario"
        else:
            salario = self.salario
        
        mensaje = f"    {self.rol}\nNombre: {self.nombre} - {self.id}\nUsuario: {self.usuario}\nSalario: {salario}"
        return mensaje
    
    def AñadirSalario(self, autor:object,  nuevo_salario: int):
        """Añade un valor entero en el argumento salario del objeto Usuario
        
        Args:
            autor (Usuario): Objeto con el argumento rol asignado como ADMINISTRADOR
            nuevo_salario (int): Valor que se va a asignar al argumento salario
        Returns:
            int: Remuneración mensual que se le da al Usuario por sus servicios
        """
        inicial_u = ""
        for letra in autor.usuario:
            if len(inicial_u) != 3:
                inicial_u += letra
            else:
                pass
                        
        if inicial_u == "adm" and autor.id[0] =="A":
            self.salario = nuevo_salario
        else:
            return "No cuenta con los permisos para hacer esto"
    
    def AumentarSalario(self, autor: object, dinero_adicional: int):
        """Modifica el argumento salario del objeto Usuario, sumandole un valor entero

        Args:
            autor (Usuario): Objeto con el argumento rol asignado como ADMINISTRADOR
            dinero_adicional (int): Valor entero a sumar en el argumento salario del Usuario

        Returns:
            int: Remuneración mensual modificada que se le da al Usuario por sus servicios
        """
        inicial_u = ""
        for letra in autor.usuario:
            if len(inicial_u) != 3:
                inicial_u += letra
            else:
                pass
        
        if inicial_u == "adm" and autor.id[0] =="A":
            self.salario += dinero_adicional
        else:
            return "No cuenta con los permisos para hacer esto"
        
    def DisminuirSalario(self, autor: object, dinero_descontable: int):
        """Modifica el argumento salario del objeto Usuario, restandole un valor entero

        Args:
            autor (Usuario): Objeto con el argumento rol asignado como ADMINISTRADOR
            dinero_descontable (int): Valor entero a se resta en el argumento salario del Usuario 

        Returns:
            int: Remuneración mensual modificada que se le da al Usuario por sus servicios
        """
        inicial_u = ""
        for letra in autor.usuario:
            if len(inicial_u) != 3:
                inicial_u += letra
            else:
                pass
        
        if inicial_u == "adm" and autor.id[0] =="A":
            self.salario -= dinero_descontable
        else:
            return "No cuenta con los permisos para hacer esto"
    
    def Promover(self, autor: object, nuevo_rol: str):
        """Subir o generar una promoción al rol del usuario, sin degradar el antes mencionado

        Args:
            autor (Usuario): Objeto con el argumento rol asignado como ADMINISTRADOR
            nuevo_rol (str): Str el cual remplaza el rol del argumento rol del objeto Usuario

        Returns:
            str: rol o papel que el usuario cumple en la organización
        """
        inicial_u = ""
        for letra in autor.usuario:
            if len(inicial_u) != 3:
                inicial_u += letra
            else:
                pass
        
        if inicial_u == "adm" and autor.id[0] =="A":
            if self.rol == nuevo_rol:
                return "No se puede ascender al mismo rol"
            elif nuevo_rol == "INVITADO":
                return "El rol invitado no puede ser usado"
            elif self.rol != nuevo_rol:
                if self.rol == "SUPERVISOR" and nuevo_rol == "CAJERO":
                    return "No puedes hacer este cambio de roles"
                elif self.rol == "ADMINISTRADOR" and (nuevo_rol == "CAJERO" or nuevo_rol == "ADMINISTRADOR"):
                    return "No puedes hacer este cambio de roles"
                else:
                    self.rol = nuevo_rol
        else:
            return "No cuenta con los permisos para hacer esto"
    
    def CambiarContraseña(self, autor: object):
        """Cambia el valor confidencial cotraseñade un Usuario, verifica la contraseña nueva antes de actualizar el valor de este
    
        Args:
            autor (Usuario): Objeto con el argumento rol asignado "ADMINISTRADOR" o el mismo Usuario sobre el cual se ejerce el metodo            

        Returns:
            Str : argumento contraseña del objeto Usuario con un nuevo valor
        """
        inicial_u = ""
        for letra in autor.usuario:
            if len(inicial_u) != 3:
                inicial_u += letra
            else:
                pass
        
        if (autor.id[0] == "A" and inicial_u == "adm")  or (self.nombre == autor.nombre):
            c_antigua = input("Ingrese su antigua contraseña: ")
            
            if c_antigua == self.contraseña:
                c_nueva = input("Ingrese su nueva contraseña: ")
                c_verifiacion =  input("Verifique la nueva contraseña: ")
                
                if c_nueva == c_verifiacion:
                    self.contraseña = c_nueva
                    return "Contraseña cambiada con exito"
                else:
                    return "Las constraseñas no coiciden"
            else:
                return "La contraseña antigua no coincide con la ingresada"
        else:
            return "Usted no cuenta con los permisos requeridos para esta acción"
    
