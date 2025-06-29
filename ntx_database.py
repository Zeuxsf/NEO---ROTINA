import sqlite3

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

def descobrir_id(nome_antigo,descricao_antiga,dia_semana):
    dados = carregar_rotina(dia_semana)
    for linha in dados:
        if linha[1] == nome_antigo and linha[2] == descricao_antiga and linha[3] == dia_semana:
            return linha[0]        

def carregar_rotina(dia):
    criar_tabela()
    cursor.execute('''SELECT * FROM trax WHERE dia = ?''', (dia,))
    return cursor.fetchall()    

def encerrar_conexao():
    conexao.close()