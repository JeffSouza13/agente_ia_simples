import sqlite3 as sql

def criar_banco():
    conn = sql.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL
        )''')
    
    conn.commit()
    conn.close()
