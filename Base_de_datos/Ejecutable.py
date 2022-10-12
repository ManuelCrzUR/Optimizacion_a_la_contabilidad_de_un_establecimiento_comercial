'''
Este archivo tiene como finalidad ser el menú principal para el usuario. 
Será el archivo que enlace todos los documentos, módulos y clases, por este motivo se llama Ejecutable.py 
    Se busca que el usuario pueda inicialmente crear usuarios dentro de la base de datos creada para el programa.
'''

#Se importan los modulos de las subcarpetas correspondientes

from Usuarios import *
from Base_de_datosUsr import *

#Bienvenida al usuario y preguntamos primero si es alguien registrado, para mayor privacidad del establecimiento.
def InicioBienvenida():
    print("Hola! Bienvenid@ a nuestro programa. \n El objetivo es optimizar manejo de contabilidad una empresa que maneje inventario y flujo de caja.")
    user_validation = input("Es usted un usuario registrado? \n [S/N]:")
    
    if user_validation.upper() == "S":
        Validacion()
    else:
        print("Lo siento, No cuentas con los permisos para acceder")
        InicioBienvenida()

def Validacion():
       
    credenciales = [] 
    user_identificacion = input("Por favor, digite su usario: \n")
    user_password = input("Digite su contraseña: \n")
    credenciales = [user_identificacion, user_password]
        
    verificador_base = Filtrar("usuario", f"{user_identificacion}")
    
    if len(verificador_base) == 0:
        if verificador_base[5] == user_password:
            print(f"Bienvenido {verificador_base[1]}")
            id_usuario = verificador_base[3]
            VerificacionRol(id_usuario)
        else:
            print("La contraseña ingresada no coincide")
            Validacion()
    else:
        print("No se encuentran usuarios en común")
        Validacion()

def VerificacionRol(id):
    inicial_id = ""
    for id in range(1):
        inicial_id += 1
    
    # if 
    
    
    #     if 
        
    #     if credenciales == ["ADMINISTRADOR", '1234']:
    #         es_administrador = credenciales 
    #         return administrador(credenciales)
    #     elif credenciales == ["CAJERO",'1234']:
    #         return cajero(credenciales)

def administrador (credenciales):
    if credenciales == ["ADMINISTRADOR", '1234']: #Esto se puede hacer dentro de una funcion llamada administrador
        eleccion = int(input("El menu de acciones es el siguiente: \n 1: Crear Usuario. \n 2: Remover usuario.\n 3: Ver o editar inventario \n 4: Imprimir facturas \n 5: Mostar modo cajero \n 6: Menu cajero \n"))
            #esto se puede optimizar con un ciclo for. De momento es funcional.
        if eleccion == 1:
                agregar = print("Aqui puede crear nuevos usarios en a la organizacion.")
                Usuarios.append(agregar) #Se comunica con el archivo Usuarios para que pueda usar el método crear usuarios implementado en dicha clase.
                return True
        elif eleccion == 2:
                quitar = print("Que usuario desea remover?") ##Se comunica con el archivo Usuarios para que pueda usar el método crear usuarios implementado en dicha clase.
                Usuarios.pop(quitar) #Al ser una lista, se implementa de la manera .pop() para remover un usuario.
                return True
        elif eleccion == 3:
                sub_opcion = int(input("Presione 1 si desea unicamente ver el inventario. \n Presione 2 si desea editar el inventario actual."))
                if sub_opcion == 1:
                    print(Base_de_datosUsr.sqlite3()) #Opcion netamente ilustrativa, porque imprimirá un archivo .txt con la informacion que contegna la base de datos.
                elif sub_opcion == 2:
                    print("Agregara un nuevo elemento?")
                    if sub_opcion.upper() == "S":
                        Base_de_datosUsr #Aqui se llama a la funcion Base de datos para agregar nuevos elementos a la lista
                    else:
                        print(Base_de_datosUsr.LeerBase)
                elif eleccion == 4: #Como el módulo 4 no se ha implementado todavía, al momento del programa notificar un error, es mejor que se le notifique al usuario que se está trabajando en ello.
                    try:
                        print(Base_de_datosUsr.FacturaCompra) 
                    except:
                        print("Pronto podra imprimir facturacion de los elementos vendidos")
                elif eleccion == 5: 
                        try:
                            Base_de_datosUsr(menu_ventas) #Pendiente por crear el menu ventas
                        except:
                            print("Oops! Este modulo pronto estara disponible")
                elif eleccion == 6:
                    Usuarios.CambiarContraseña() #En este método, el programa se comunicará con Usuario y el método Cambiar Contraseña
    else:
        return "Contacte a su administrador para que le pueda crear su usuario."        

def cajero(credenciales):
        if credenciales == ["CAJERO", 1234]: #El usuario cajero, tiene unicamente permitido usar metodos de facturacion e inventario
            print("Bienvenido de vuelta, " + user_identificacion)
            cajero_eleccion = int(input("Presione 1 para empezar a facturar. \n Presione 2 para mirar el inventario actual."))
            if cajero_eleccion == 1:
                Base_de_datosUsr.CrearTabla()
            elif cajero_eleccion == 2:
                print(Base_de_datosUsr.LeerBase())
            else:
                return 'Escoja una opcion valida'

def supervisor(credenciales):
    if credenciales == ["SUPERVISOR", 1234]:
        print("Bienvenido de vuelta, " + user_identificacion)
        supervisor_eleccion = int(input("El menu de acciones es el siguiente: \n 1: Ver o editar inventario \n 2: Imprimir facturas \n 3: Mostar modo cajero \n 6: Menu cajero"))
        if supervisor_eleccion == 1:
            sub_opcion = int(input("Presione 1 si desea unicamente ver el inventario. \n Presione 2 si desea editar el inventario actual."))
            if sub_opcion == 1:
                print(Base_de_datosUsr.sqlite3())
            elif sub_opcion == 2:
                print("Agregara un nuevo elemento?")
                if sub_opcion.upper() == "S":
                    Base_de_datosUsr #Aqui se llama a la funcion Base de datos para agregar nuevos elementos a la lista
                else:
                    print(Base_de_datosUsr.LeerBase)
            elif supervisor_eleccion == 2: 
                try:
                    print(Base_de_datosUsr.FacturaCompra) 
                except:
                    print("Pronto podra imprimir facturacion de los elementos vendidos")
            elif supervisor_eleccion == 3: 
                try:
                    Base_de_datosUsr(menu_ventas) #Pendiente por crear el menu ventas
                except:
                    print("Oops! Este modulo pronto estara disponible")
            elif credenciales == ['INVITADO', 1234]:
                print("Como invitado usted puede unicamente ver el inventario del establecimiento.")
                return Base_de_datosUsr.LeerBaseOrdenada
    else: 
        return "Contacte a su administrador para que le pueda crear su usuario" 

#Se llama a la funcion para validar su funcionamiento
InicioBienvenida()


