'''
Este archivo tiene como finalidad ser el menú principal para el usuario. 
Será el archivo que enlace todos los documentos, módulos y clases, por este motivo se llama Ejecutable.py 
    Se busca que el usuario pueda inicialmente crear usuarios dentro de la base de datos creada para el programa.
'''

#Se importan los modulos de las subcarpetas correspondientes

import Usuarios
# from Usuarios import CambiarContraseña 
import Base_de_datosUsr

print("Hola! Bienvenid@ a nuestro programa. \n El objetivo es optimizar el portafolio de una empresa que maneje inventario y flujo de caja.")
user_validation = input("Es usted un usuario registrado? \n [S/N]:")

def validacion(user_validation):
    
    if user_validation.upper() == "S":
        credenciales = ""
        user_identificacion = input("Por favor, digite su usario: \n")
        user_password = input("Digite su contraseña: \n")
        credenciales = (user_identificacion, user_password)
        # return credenciales
        if credenciales == "ADMINISTRADOR": #Esto se puede hacer dentro de una funcion llamada administrador
            eleccion = print(int("El menu de acciones es el siguiente: \n 1: Crear Usuario. \n 2: Remover usuario.\n 3: Ver o editar inventario \n 4: Mas opciones."))
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
        # elif credenciales.upper() == "CAJERO": 
        #     print("Bienvenido de vuelta, " + user_identificacion)
        #     cajero_eleccion = int(input())
    else: 
        return "Contacte a su administrador para que le pueda crear su usuario."

validacion(user_validation)
# if user_validation == usario_registrado:
#     print("Bienvenid@ de vuelta, " + usuario_registado)
# opcion_usuario = input("El menú de opciones es el siguiente: \n 1: Crear usuario \n 2: Visualizar usuarios activos \n 3: ")
# 1. crear usauruis
# 2. base de Datos
# 3. buscar cusarios

