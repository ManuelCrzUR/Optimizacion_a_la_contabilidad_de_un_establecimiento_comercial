'''
Este archivo tiene como finalidad ser el menú principal para el usuario. 
Será el archivo que enlace todos los documentos, módulos y clases, por este motivo se llama Ejecutable.py 
    Se busca que el usuario pueda inicialmente crear usuarios dentro de la base de datos creada para el programa.
'''

#Se importan los modulos de las subcarpetas correspondientes

import Usuarios
# from Usuarios import CambiarContraseña 
import Base_de_datosUsr

print("Hola! Bienvenid@ a nuestro programa. \n El objetivo es optimizar manejo de contabilidad una empresa que maneje inventario y flujo de caja.")
user_validation = input("Es usted un usuario registrado? \n [S/N]:")

def validacion(user_validation):
    
    if user_validation.upper() == "S":
        credenciales = ""
        user_identificacion = input("Por favor, digite su usario: \n")
        user_password = input("Digite su contraseña: \n")
        credenciales = [user_identificacion, user_password]
        print (credenciales)

        if credenciales == ["ADMINISTRADOR", '1234']: #Esto se puede hacer dentro de una funcion llamada administrador
            eleccion = int(input("El menu de acciones es el siguiente: \n 1: Crear Usuario. \n 2: Remover usuario.\n 3: Ver o editar inventario \n 4: Imprimir facturas \n 5: Mostar modo cajero \n 6: Menu cajero"))
            #esto se puede optimizar con un ciclo for.
            if eleccion == 1:
                agregar = print("Aqui puede crear nuevos usarios en a la organizacion.")
                Usuarios.append(agregar) #mejorar esta linea, no lleva a nada de momento.
            elif eleccion == 2:
                quitar = print("Que usuario desea remover?")
                Usuarios.pop(quitar)
            elif eleccion == 3:
                sub_opcion = int(input("Presione 1 si desea unicamente ver el inventario. \n Presione 2 si desea editar el inventario actual."))
                if sub_opcion == 1:
                    print(Base_de_datosUsr.sqlite3())
                elif sub_opcion == 2:
                    print("Agregara un nuevo elemento?")
                    if sub_opcion.upper() == "S":
                        Base_de_datosUsr #Aqui se llama a la funcion Base de datos para agregar nuevos elementos a la lista
                    else:
                        print(Base_de_datosUsr.LeerBase)
            elif eleccion == 4: 
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
                Usuarios.CambiarContraseña()
        elif credenciales == ["CAJERO",1234]: 
            print("Bienvenido de vuelta, " + user_identificacion)
            cajero_eleccion = int(input("Presione 1 para empezar a facturar. \n Presione 2 para mirar el inventario actual."))
            return cajero_eleccion
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

validacion(user_validation)


