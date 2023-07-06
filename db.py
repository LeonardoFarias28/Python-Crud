# Importando SQLite

import sqlite3 as lite

# Criando conexão

con = lite.connect('dados.db')

# criando tabela

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formuylario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")
