import sqlite3
import sys
import os

#Função para localizar imagens e sons na hora de criar o executável
def caminho(item):
    try:
        caminho_base = sys._MEIPASS
    except AttributeError:
        caminho_base = os.path.abspath('.')
    return os.path.join(caminho_base,item)        

def database():
    conexao = sqlite3.connect('neotrax.db')
    cursor = conexao.cursor()
    
    return conexao, cursor

conexao, cursor = database()

def criar_tabela():
    cursor.execute('''CREATE TABLE IF NOT EXISTS trax (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        descricao TEXT,
        dia TEXT,
        inicio TEXT,
        fim TEXT,
        temporario INTEGER DEFAULT 1,
        checkbox INTEGER DEFAULT 2,
        pontos INTEGER DEFAULT 0);''')

def adicionar_linha(nome,descricao,dia,inicio,fim,temporario):
    criar_tabela()
    cursor.execute('''INSERT INTO trax (nome,descricao,dia,inicio,fim,temporario)
                   VALUES (?,?,?,?,?,?)''',(nome,descricao,dia,inicio,fim,temporario))
    
    conexao.commit()

def excluir_linha(id):
    cursor.execute('''DELETE FROM trax WHERE id = ?''', (id,))
    conexao.commit()

def editar_linha(id,nome,descricao):
    cursor.execute('''UPDATE trax SET nome = ?, descricao = ? WHERE id = ?''',(nome,descricao,id))
    conexao.commit()

def descobrir_id(nome_antigo,descricao_antiga,dia_semana,temporario):
    dados = carregar_rotina(dia_semana)
    for linha in dados:
        if linha[1] == nome_antigo and linha[2] == descricao_antiga and linha[3] == dia_semana and linha[6] == temporario:
            return linha[0]        

def carregar_rotina(dia):
    criar_tabela()
    cursor.execute('''SELECT * FROM trax WHERE dia = ?''', (dia,))
    return cursor.fetchall()    

def buscar_pontos_totais(dia,tipo='geral'):
    if tipo == 'geral':
        cursor.execute('''SELECT SUM(pontos) FROM trax WHERE dia = ?''', (dia,))
        pontos = cursor.fetchone()
        try:
            pontos = int(pontos[0])
        except:
            pontos = 0  
        return pontos
    elif tipo == 'tarefa':
        try:
            cursor.execute('''SELECT nome FROM trax WHERE dia = ? ORDER BY pontos DESC LIMIT 1''', (dia,))
            resultado = cursor.fetchone()
            taf = str(resultado[0]).lower()
        except:
            taf = 'N/A'    
        return taf

def media_pontos():
    cursor.execute('''SELECT AVG(pontos) FROM trax''')
    pontos = cursor.fetchone()
    try:
        pontos = f'{float(pontos[0]):.2f}'
    except Exception as e:
        pontos = 0
        print(e)
    return pontos
    
def reset():
    cursor.execute('''DELETE FROM trax''')
    cursor.execute('''DELETE FROM sqlite_sequence WHERE name="trax"''')
    conexao.commit()

    
def encerrar_conexao():
    conexao.close()