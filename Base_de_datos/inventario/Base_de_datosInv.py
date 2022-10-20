from Productos import *
import sqlite3

def CrearBaseInventario():
    conn = sqlite3.connect('Inventario.db')
    conn.commit()
    conn.close()
    
def CrearTablaInventario():
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    abrir_table = f"""CREATE TABLE IF NOT EXISTS inventario (
        producto TEXT,
        division TEXT,
        precio_unitario INTEGER,
        cantidad INTEGER,
        )"""
    cursor.execute(abrir_table)
    conn.commit()
    conn.close()

def OrdenarBase():
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    leer_ordenado = f"SELECT * FROM inventario ORDER BY division"
    cursor.execute(leer_ordenado)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

def LeerBaseInv():
    OrdenarBase()
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    leer = f"SELECT * FROM inventario"
    cursor.execute(leer)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def InsertarProducto(producto):
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    ejecutable = f"INSERT INTO inventario VALUES ('{producto.name}', '{producto.division}', '{producto.precio_unitario}', '{producto.cantidad}')" 
    cursor.execute(ejecutable)
    OrdenarBase()
    conn.commit()   
    conn.close()
    
def ActualizarPrecio(producto, precio):
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    instr = f"SELECT * FROM inventario WHERE producto == '{producto}'"
    conn.execute(instr)
    nombr = instr[0]
    divis = instr[1]
    cant = instr[3]
    instr2 = f"DELETE FROM inventario WHERE producto == '{producto}'"
    cursor.execute(instr2)
    OrdenarBase()
    conn.commit()
    conn.close()
    prd = Productos(nombr, divis, precio, cant)
    InsertarProducto(prd)
    
def ActualizarCantidad(producto, cantidad):
    conn = sqlite3.connect('Inventarios.db')
    cursor = conn.cursor()
    instr = f"SELECT * FROM inventario WHERE prducto == '{producto}'"
    conn.execute(instr)
    nombr = instr[0]
    divis = instr[1]
    prec = instr[2]
    instr2 = f"DELETE FROM inventario WHERE producto == '{producto}'"
    cursor.execute(instr2)
    OrdenarBase()
    conn.commit()
    conn.close()
    prd = Productos(nombr, divis, prec, cantidad)
    InsertarProducto(prd)

def Filtrar(argumento, filtro): 
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM producto WHERE {argumento} == '{filtro}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos    

def EliminarProducto(nombre):
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    instr = f"DELETE FROM producto WHERE producto == '{nombre}'"
    cursor.execute(instr)
    conn.commit()
    conn.close()
    