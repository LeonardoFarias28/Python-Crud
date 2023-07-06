# Importando SQLite

import sqlite3 as lite
import pandas as pd

#C = Inserir / Criar
#Ready = Acessar / Mostrar
#Update = Atualizar
#Delete = Deletar / Apagar

# criando conexão
con = lite.connect('dados.db')


# inserir informações
def inserirInfo(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formuylario (nome, email, telefone , dia_em, estado , assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)

# Acessar informações
def mostrarInfo():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formuylario"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista
       # Atualizar informações 
            
def atualizarInfo(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formuylario SET nome=? , email=?, telefone=?, dia_em=? , estado=?, assunto=? WHERE id=?"
        cur.execute(query,i)
    
# Deletar informações
def deletarInfo(i):
    with con:
        cur = con.cursor()
        query = "DELETE fROM formuylario WHERE id=?"
        cur.execute(query,i)
        
