import customtkinter as ctk
import json
import conteudo_rotina as cr
import os

arquivo_rotina = 'dadosrotina.json'

def carregar_rotina(arquivo_rotina):
    if os.path.exists(arquivo_rotina):
        try:
            with open(arquivo_rotina,'r') as file:
                dados = json.load(file)
                return dados    
        except (FileNotFoundError , json.JSONDecodeError):
            return  {}
    else:
       return  {}

def salvar_rotina(arquivo_rotina,dados):
    with open(arquivo_rotina,'w') as file:
        json.dump(dados,file,indent=4,ensure_ascii=True)         

