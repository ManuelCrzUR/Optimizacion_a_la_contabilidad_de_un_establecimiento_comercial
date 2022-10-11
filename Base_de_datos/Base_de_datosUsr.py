import sqlite3

def CrearBase():
    conn = sqlite3.connect('Miembros.db')
    conn.commit()
    conn.close()
    
def CrarTabla():
    conn = sqlite3.connect('Miembros.db')
    cursor = conn.cursor()
    cursor.execut(
        """CREATE TABLE IF NOT EXISTS usuarios (
            rol TEXT,
            nombre TEXT,
            salario INTEGER,
            id TEXT,
            usuario TEXT,
            contraseña TEXT
        )"""
    )
    conn.commit()
    conn.close()     
    
def InsertarUsuario(usr):
    conn = sqlite3.connect('Miembros.db')
    cursor = conn.cursor()
    añadir = f"INSERT INTO usuarios VALUES ('{usr.rol}', '{usr.nombre}', '{usr.salario}','{usr.id}', '{usr.usuario}', '{usr.contraseña}')"
    cursor.execute(añadir)
    conn.commit()
    conn.close()
    
def InsertarVariosUsuarios(usr_lista):
    conn = sqlite3.connect('Miembros.db')
    cursor = conn.cursor()
    añadir = f"INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?)"
    cursor.executemany(añadir, usr_lista)
    conn.commit()
    conn.close()

def LeerBase():
    conn = sqlite3.connect('Miembros.db')
    cursor = conn.cursor()
    leer = f"SELECT * FROM usuarios"
    cursor.execute(leer)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
    
def LeerBaseOrdenada(campo):
    conn = sqlite3.connect('Miembros.db')
    cursor = conn.cursor()
    leer_ordenado = f"SELECT * FROM usuarios ORDERED BY {campo}"
    cursor.execute(leer_ordenado)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
    