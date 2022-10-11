'''
Este archivo tiene como finalidad ser el menú principal para el usuario. 
Será el archivo que enlace todos los documentos, módulos y clases, por este motivo se llama Ejecutable.py 
    Se busca que el usuario pueda inicialmente crear usuarios dentro de la base de datos creada para el programa.
'''

#Se importan los modulos de las subcarpetas correspondientes

import Usuarios
import U_prueba_Usuarios
# from Usuarios import CambiarContraseña 
import Base_de_datosUsr

#Bienvenida al usuario y preguntamos primero si es alguien registrado, para mayor privacidad del establecimiento.
print("Hola! Bienvenid@ a nuestro programa. \n El objetivo es optimizar manejo de contabilidad una empresa que maneje inventario y flujo de caja.")
user_validation = input("Es usted un usuario registrado? \n [S/N]:")

'''
    Dentro de la función validación, la idea es que el programa identifique qué tipo de usuario está intentando ingresar al programa.
    Las credenciales son cotejadas con la base de datos. 
    En caso de ser un usuario registrado se le proporcionarán diferentes opciones. El usuario Administrador contiene todas las opciones disponibles en el programa.

    En caso ser personal no autorizado, se le pedirá al usuario que contacte un administrador para que le cree una cuenta y poder usar el programa.

'''

def validacion(user_validation):
    '''
        Usuarios existentes:
        Administrador que puede usar cualquier modulo del programa.
        Supervisor: tiene opciones de caja y parcialmente de administrador.
        Cajero: Tiene opciones netamente operativas
        Invitado: Solo puede visualizar datos superficiales.

    '''
    if user_validation.upper() == "S": #La respuesta del usuario se globaliza a mayúsculas por practicidad.
        credenciales = "" #Se genera una tupla vacía que contendrá el ingreso de la información confidencial.
        user_identificacion = input("Por favor, digite su usario: \n")
        user_password = input("Digite su contraseña: \n")
        credenciales = [user_identificacion, user_password]
        #print (credenciales) para verificar que esté tomando los datos

        if credenciales == ["ADMINISTRADOR", '1234']: #Esto se puede hacer dentro de una funcion llamada administrador
            eleccion = int(input("El menu de acciones es el siguiente: \n 1: Crear Usuario. \n 2: Remover usuario.\n 3: Ver o editar inventario \n 4: Imprimir facturas \n 5: Mostar modo cajero \n 6: Menu cajero"))
            #esto se puede optimizar con un ciclo for. De momento es funcional.
            if eleccion == 1:
                agregar = print("Aqui puede crear nuevos usarios en a la organizacion.")
                Usuarios.append(agregar) #Se comunica con el archivo Usuarios para que pueda usar el método crear usuarios implementado en dicha clase.
            elif eleccion == 2:
                quitar = print("Que usuario desea remover?") ##Se comunica con el archivo Usuarios para que pueda usar el método crear usuarios implementado en dicha clase.
                Usuarios.pop(quitar) #Al ser una lista, se implementa de la manera .pop() para remover un usuario.
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
        elif credenciales == ["CAJERO",1234]: #El usuario cajero, tiene unicamente permitido usar metodos de facturacion e inventario
            print("Bienvenido de vuelta, " + user_identificacion)
            cajero_eleccion = int(input("Presione 1 para empezar a facturar. \n Presione 2 para mirar el inventario actual."))
            if cajero_eleccion == 1:
                Base_de_datosUsr.CrearTabla()
            elif cajero_eleccion == 2:
                print(Base_de_datosUsr.LeerBase())
            else:
                return 'Escoja una opcion valida'

        elif credenciales == ["SUPERVISOR", 1234]:
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
        print("Contacte a su administrador para que le pueda crear su usuario.") 

#Se llama a la funcion para validar su funcionamiento
validacion(user_validation)


