from Usuarios import *
import sqlite3

def CrearBase():
    conn = sqlite3.connect('Miembros.db')
    conn.commit()
    conn.close()
    
def CrarTabla():
    conn = sqlite3.connect('Miembros.db')
    cursor = conn.Cursor()
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
    
def InstertarUsuario(Usuario):
    conn = sqlite3.connect()
    cursor = conn.cursor()
    instruccion = "INSERT"
    