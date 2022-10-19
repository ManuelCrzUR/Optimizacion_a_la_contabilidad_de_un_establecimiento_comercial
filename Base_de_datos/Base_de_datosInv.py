import sqlite3

def CrearBaseInventario():
    conn = sqlite3.connect('Inventario.db')
    conn.commit()
    conn.close()
    
def CrearTablaInventario(division):
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    abrir_table = f"""CREATE TABLE IF NOT EXISTS {division} (
        producto TEXT,
        precio_unitario INTEGER,
        cantidad INTEGER,
        )"""
    cursor.execute(abrir_table)
    conn.commit()
    conn.close()

def OrdenarBase(division):
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    leer_ordenado = f"SELECT * FROM {division} ORDER BY producto"
    cursor.execute(leer_ordenado)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

def LeerBaseInv(division):
    OrdenarBase(division)
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    leer = f"SELECT * FROM {division}"
    cursor.execute(leer)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos


def InsertarProducto(division, producto):
    OrdenarBase(division)
    conn = sqlite3.connect('Inventario.db')
    cursor = conn.cursor()
    ejecutable = f"INSERT INTO {division} VALUES ('{producto.name}', '{producto.precio_unitario}', '{producto.cantidad}')" 
    cursor.execute(ejecutable)
    conn.commit()   
    conn.close()
    
