class Usuarios_Ad:
    def __init__(self, nombre, contraseña):
        self.usuario_administrador = nombre
        self.contraseña = contraseña
        self.confirmacion = False

    def CrearAdministrador(self, nombre_nuevo):
        import importlib.util

        spec = importlib.util.spec_from_file_location("Usuarios", ".Proyecto_Programacion/Base_de_datos/Usuarios.py")
        Usr = importlib.util.mocule_from_spec
        print(Administradores)
        comprobacion_Adm  = input("Ingrese el Usuario Autorizado")



Usuario_supremo = Usuarios_Ad("Usuario-Principal", 123456789)

print(Usuario_supremo.CrearAdministrador("Jose"))