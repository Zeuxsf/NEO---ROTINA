import customtkinter as ctk
import json
import os
import ntx_database as db
from PIL import Image
import winreg
import sys

arquivo = 'ntx_configs.json'

#Função para carregar o arquivo json
def carregar_configs():   
   try:
      with open('ntx_configs.json','r') as file:
         dados = json.load(file)
         return dados    
   except Exception as e:
      print(e)
      return  {'usuario': 'usuario_1', 'p_tempo':25,'p_descanso':5,'iniciar_windows':True}

#Função para salvar os dados alterados no arquivo
def salvar_configs(dados,nome,p_tempo,p_descanso,iniciar,janela,tela_principal):
   dados['usuario'] = nome
   dados['p_tempo'] = p_tempo
   dados['p_descanso'] = p_descanso
   dados['iniciar_windows'] = iniciar
     
   with open('ntx_configs.json','w') as file:
        json.dump(dados,file,indent=4,ensure_ascii=False)
   
   if iniciar == True:
      iniciar_com_windows(True)
   else:
      iniciar_com_windows(False)   
       
   config(janela,tela_principal)
                 

#Função para resetar todo o banco de dados + o arquivo de configurações
def reset(janela,tela_principal):
      if os.path.exists(arquivo):
         os.remove(arquivo)
      db.reset()
      if os.path.exists('ntx_configs.json') == False:
         salvar_configs(carregar_configs(),'usuario_123',25,5,True,janela,tela_principal)

#Função para fazer o programa iniciar (ou não) com o computador
def iniciar_com_windows(indicador=True):
   try:
      nome_programa = 'NeoTrax'
      caminho = os.path.abspath(sys.argv[0])
      chave = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_SET_VALUE)
      
      if indicador == True:
         winreg.SetValueEx(chave,nome_programa,0,winreg.REG_SZ,caminho)
         winreg.CloseKey(chave)
      else:
            winreg.DeleteValue(chave,nome_programa)
            winreg.CloseKey(chave)
   except FileNotFoundError:
         pass                  

#Tela de Configurações
def config(janela,tela_principal):
 for widget in janela.winfo_children():
    widget.destroy()

 tela_principal.geometry('1000x650')    
 titulo = ctk.CTkLabel(janela,text='Configurações',font = ('',30))
 titulo.place(x=330,y=10)
 
 dados = carregar_configs()
 
 #Nome de usuário
 u_titulo = ctk.CTkLabel(janela,width=1100,height=20,text='Usuário',fg_color='gray7',text_color='gray69')
 u_titulo.place(x=-125,y=75)
 u_subtitulo = ctk.CTkLabel(janela, text='Nome de Usuário')
 u_subtitulo.place(x=380, y=100) 
 
 usuario_nome = ctk.CTkEntry(janela,width=400,height=20,placeholder_text='usuário',fg_color='gray4',border_color='gray23',text_color='gray69')
 usuario_nome.place(x=215,y=130)
 usuario_nome.insert(0,str(dados['usuario']))
 
 #Timers pro pomodoro
 p_titulo = ctk.CTkLabel(janela,width=1100,height=20,text='Pomodoro (Minutos)',fg_color='gray7',text_color='gray69')
 p_titulo.place(x=-125,y=180)
 p_subtitulo = ctk.CTkLabel(janela, text="Timer de Produtividade                                                        Timer de Descanso")
 p_subtitulo.place(x=210, y=210)
 
 p_tempo = ctk.CTkOptionMenu(master=janela,values=['25','30','35','40','45','50','55','60'],fg_color='gray9',button_color='gray23',button_hover_color='gold3',text_color='gray69',width=100)
 p_tempo.place(x=215,y=235)
 p_tempo.set(dados['p_tempo'])
 
 p_descanso = ctk.CTkOptionMenu(master=janela,values=['5','10','15','20','25','30'],fg_color='gray9',button_color='gray23',button_hover_color='gold3',text_color='gray69',width=100)
 p_descanso.place(x=512,y=235)
 p_descanso.set(dados['p_descanso'])
 
 #Definir se inicia ou não com o sistema
 ini_titulo = ctk.CTkLabel(janela,width=1100,height=20,text='Sistema',fg_color='gray7',text_color='gray69')
 ini_titulo.place(x=-125,y=300)
 ini_var = ctk.BooleanVar(value=dados['iniciar_windows'])

 ini_escolha = ctk.CTkRadioButton(janela, text="NÃO Iniciar com o Sistema", variable=ini_var, value=False,fg_color='red',hover_color='brown')
 nao_ini_escolha = ctk.CTkRadioButton(janela, text="Iniciar com o Sistema", variable=ini_var, value=True,fg_color='yellow',hover_color='gold3')
 
 ini_escolha.place(x=215, y=343)
 nao_ini_escolha.place(x=512, y=343)
 
 #Salva as alterações
 salvar_btn = ctk.CTkButton(janela,width=20,height=20,text='✓ Salvar Alterações',command=lambda:salvar_configs(dados,usuario_nome.get(),p_tempo.get(),p_descanso.get(),ini_var.get(),janela,tela_principal),fg_color='yellow',hover_color='gold3',text_color='gray2',font=('',20))
 salvar_btn.place(x=658,y=455)
 
 #Reseta tudo: banco de dados, configs
 resetar_btn_image = ctk.CTkImage(Image.open('imagens/reiniciar.png'),size=(40,40))
 reset_btn = ctk.CTkButton(janela,20,20,text='Resetar Programa',font=('',20),command=lambda:reset(janela,tela_principal),fg_color='transparent',hover_color='red',text_color='yellow',image=resetar_btn_image)
 reset_btn.place(x=620,y=520)
 r_subtitulo = ctk.CTkLabel(janela, text="(Use apenas se quiser apagar todos os dados e tarefas do programa e retornar ao padrão)",wraplength=300)
 r_subtitulo.place(x=590, y=570) 
   