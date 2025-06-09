import customtkinter as ctk
import json
import conteudos.conteudo_rotina as cr
import os

pasta_destino = 'rotina'

def carregar_rotina(dia_semana):
    
    os.makedirs(pasta_destino,exist_ok=True)
    caminho_arquivo = os.path.join(pasta_destino, f'{dia_semana}_rotina.json')
    
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo,'r') as file:
                dados = json.load(file)
                return dados    
        except (FileNotFoundError , json.JSONDecodeError):
            return  {}
    else:
       return  {}

def salvar_rotina(dia_semana,dados):
    
    os.makedirs(pasta_destino,exist_ok=True)
    caminho_arquivo = os.path.join(pasta_destino, f'{dia_semana}_rotina.json')
    
    with open(caminho_arquivo,'w') as file:
        json.dump(dados,file,indent=4,ensure_ascii=False)         

def carregar_pontos():
    os.makedirs(pasta_destino,exist_ok=True)
    caminho_arquivo = os.path.join(pasta_destino, f'pontuação_rotina.json')
    
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo,'r') as file:
                dados = json.load(file)
                return dados    
        except (FileNotFoundError , json.JSONDecodeError):
            return  {
                "pontos": 0
            }
    else:
       return  {
           "pontos": 0
       }

    

def salvar_pontos(quantidade,dados):
    os.makedirs(pasta_destino,exist_ok=True)
    caminho_arquivo = os.path.join(pasta_destino, f'pontuação_rotina.json')
    
    with open(caminho_arquivo, 'w') as file:
        json.dump(dados,file)
    
    