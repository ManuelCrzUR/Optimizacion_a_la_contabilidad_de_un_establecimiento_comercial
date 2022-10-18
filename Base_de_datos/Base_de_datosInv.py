import sqlite3

def CrearBaseInventario():
    conn = sqlite3.connect('Miembros.db')
    conn.commit()
    conn.close()
    
def CrearTablaInventario(division):
    conn = sqlite3.connect('Miembros.db')
    cursor = conn.cursor()
    abrir_table = f"""CREATE TABLE IF NOT EXISTS {division} (
        producto TEXT,
        precio_unitario INTEGER,
        cantidad INTEGER,
        )"""
    