"""Módulo U_prueba_Usuarios
    
    Este módulo se encarga de comprobar el funcionamiento de todas las funciones y metodos de la clase Usuario del módulo Usuarios mediante Unidades de Prueba
    """

from Usuarios import *
import sys

def test(pasa):
    linea_num = sys._getframe(1).f_lineno
    
    if pasa:
        msn = "test en linea {0} OK".format(linea_num)
    else:
        msn = "test en linea {0} FALLO".format(linea_num)
    print(msn)
    
usr_prueba = Usuario("prueba", "ADMINISTRADOR", "adm_001", "1", "A000")
usr_prueba2 = Usuario("prueba2", "CAJERO", "caj_001", "1", "C000")
  
def test_suite_init(): 
    test(type(usr_prueba) == Usuario)    
    
def test_suite_AñadirSalario():
    usr_prueba.AñadirSalario(usr_prueba, 10000)
    test(usr_prueba.salario == 10000)   
     
def test_suite_AumentarSalario():
    usr_prueba.AumentarSalario(usr_prueba, 5000)
    test(usr_prueba.salario == 15000)
    
def test_suite_DisminuirSalario():
    usr_prueba.DisminuirSalario(usr_prueba, 2500)
    test(usr_prueba.salario == 12500)
    
def test_suite_Promover():
    test(usr_prueba2.rol == "CAJERO")
    usr_prueba2.Promover(usr_prueba, "SUPERVISOR")
    test(usr_prueba2.rol == "SUPERVISOR")
    
def test_suite_CambiarContraseña():
    test(usr_prueba.contraseña == "1")
    usr_prueba.CambiarContraseña(usr_prueba)
    test(usr_prueba.contraseña == "0")

if __name__ == "__main__":    
    test_suite_init()
    test_suite_AñadirSalario()
    test_suite_AumentarSalario()
    test_suite_DisminuirSalario()
    test_suite_Promover()
    test_suite_CambiarContraseña()