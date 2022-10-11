import sys

def test(pasa):
    linea_num = sys._getframe(1).f_lineno
    
    if pasa:
        msn = "test en linea {0} OK".format(linea_num)
    else:
        msn = "test en linea {0} FALLO".format(linea_num)
    print(msn)
     
    mensaje = "Daniel es el amor de mi vida"