from Usuarios import *
import sqlite3

def InsertarUsuario(usuario):
    conectar = sqlite3.connect('usuarios.db')
    cursor = conectar.cursor()
    
    cursor.execute(f"""INSERT INTO usuarios VALUES
                   ('{usuario.rol}', '{usuario.nombre}', {usuario.salario}, '{usuario.id}', '{usuario.contraseña}')
                   """)
    
    conectar.commit()
    conectar.close()

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
    rol TEXT,
    nombre TEXT,
    salario REAL,
    usuario TEXT, 
    id TEXT,
    contraseña TEXT )""")

c = Usuario("manuel", "ADMINISTRADOR", "adm_001", "mariana", "A123", '1300')
InsertarUsuario(c)

c.execute("SELECT * FROM ususarios")
usuarios = c.fetchall()

print(usuarios)

conn.close()