import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")

cursor = conexao.cursor()

def criar_tablea(cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)

    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?', data)
    conexao.commit()