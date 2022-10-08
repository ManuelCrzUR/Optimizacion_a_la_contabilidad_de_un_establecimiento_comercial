"Módulo Usuarios"

class Usuario:
    """Representa un Usuario
    
    Atributos:
        nombre (str): [Nombre]
        rol (str): [rol]
        usuario (str): [Usuario]
        contraseña (str): [Contraseña]
        id (str): [id]
        salario (int)"""
        
    def __init__(self, Nombre: str, rol: str, Usuario: str, Contraseña: str, id: str, salario: int = None):
        """Inicializa en objeto de tipo Usuario

        Args:
            Nombre (str): Distinguidor de objeto, personal
            rol (str): Papel que este cumple en la organización
            Usuario (str): Identificador del objeto Usuario.
            Contraseña (str): Comprobador de pertenencia al Usuario.
            id (str): Identificador en al organización, da acceso a ciertas funciones.
            salario (int, opcional): Valor de remuneracion mensual. Por defecto None
        """
        self.rol = rol
        self.nombre = Nombre
        self.salario = None
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
        
        mensaje = f"    {self.rol}\nNombre: {self.nombre} - {self.id}\nUsuario: {self.usuario}\nSalario = {salario}"
        return mensaje
    
    def AñadirSalario(self, autor,  nuevo_salario: int):
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
    
    def AumentarSalario(self, autor, dinero_adicional):
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
        
    def DisminuirSalario(self, autor, dinero_descontable):
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
    
    def Promover(self, autor, nuevo_rol):
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
    
    def CambiarContraseña(self, autor, antigua_contraseña, nueva_contraseña):
        inicial_u = ""
        for letra in autor.usuario:
            if len(inicial_u) != 3:
                inicial_u += letra
            else:
                pass
        
        if autor.id[0] == "A" and inicial_u == "adm":
            c_antigua = input("Ingrese su antigua contraseña: ")
            
            if c_antigua == self.contraseña:
                c_nueva = input("Ingrese su nueva contraseña")
                c_verifiacion =  input("Verifique la nueva contraseña")
                
                if c_nueva == c_verifiacion:
                    self.contraseña = c_nueva
                    return "Contraseña cambiada con exito"
                else:
                    return "Las constraseñas no coiciden"
            else:
                return "La contraseña antigua no coincide con la ingresada"
        else:
            return "Usted no cuenta con los permisos requeridos para esta acción"
    
adm1 = Usuario("manuel", "ADMINISTRADOR", "adm_manuel", "Manu.santy2004", "A001" )
print(adm1)