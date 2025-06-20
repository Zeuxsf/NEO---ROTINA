import customtkinter as ctk
import conteudos.conteudo_rotina as conteudo_rotina 
import conteudos.conteudo_config as conteudo_config
import conteudos.conteudo_info as conteudo_info
import conteudos.conteudo_pomodoro as conteudo_pomodoro
import conteudos.conteudo_pontuacao as conteudo_pontuacao
from PIL import Image
import datetime
import winotify
import schedule
import json
import salvar_carregar as j
from unidecode import unidecode
import string



hoje = datetime.datetime.now()

ontem = hoje - datetime.timedelta(days=1)
ontem = ontem.strftime("%A")

hora = hoje.strftime("%H:%M")



#Área de cores:
dark_ou_light = 'dark'
ctk.set_appearance_mode(dark_ou_light)
if dark_ou_light == 'dark':
    cor_principal = 'dodgerblue'
else:
    cor_principal = 'red'    

#Configurações da Janela Principal
janela = ctk.CTk()
janela.geometry('1000x650')
janela.resizable(False,False)
janela.title('NeoTrax')


#Uma tela scrolável, pro programa ter liberdade de crescer
conteudo_frame = ctk.CTkScrollableFrame(janela,844,670,fg_color='transparent')
conteudo_frame.place(x=129,y=10)



#Imagens usadas no programa:
configbtn_image = ctk.CTkImage(Image.open('imagens/cfg.png'))
ajudabtn_image = ctk.CTkImage(Image.open('imagens/inf.png'))
rotina_atualbtn_image = ctk.CTkImage(Image.open('imagens/rotina_atual.png'), size=(40,40))
rotinas_btn_image = ctk.CTkImage(Image.open('imagens/rotinas.png'), size=(40,40))
pontos_btn_image = ctk.CTkImage(Image.open('imagens/pontuacao.png'), size=(40,40))
pomodoro_btn_image = ctk.CTkImage(Image.open('imagens/pomodoro.png'), size=(40,40))


#Configurações da Aba Lateral, a Navegação do programa
aba = ctk.CTkFrame(janela,120,680)
aba.place(x=1,y=-4)

#Iniciando o programa:
conteudo_rotina.rotina_atual(conteudo_frame,janela)

#Botões:

#Botão de Configuração (Configurações do programa)
configbtn = ctk.CTkButton(aba,10,10,text='',command=lambda: conteudo_config.config(conteudo_frame,janela),image=configbtn_image,fg_color='transparent',hover_color=cor_principal)
configbtn.place(x= 70,y=600)

#Botão de Ajuda (Ajuda o usuário a navegar pelo Programa, e também, mostra os créditos (autor, etc))
ajudabtn = ctk.CTkButton(aba,25,10,text='',command=lambda: conteudo_info.info(conteudo_frame,janela),image= ajudabtn_image,fg_color='transparent',hover_color=cor_principal)
ajudabtn.place(x=10,y=600)

#Botão Minha Rotina (Rotina do dia Atual)
rotina_atualbtn = ctk.CTkButton(aba,10,50,text='',image=rotina_atualbtn_image, fg_color='transparent',font=('',100), command=lambda: conteudo_rotina.rotina_atual(conteudo_frame,janela),hover_color=cor_principal)
rotina_atualbtn.place(x=33,y=35)

#Botão Rotinas (Todas as rotinas)
rotinas_btn = ctk.CTkButton(aba,10,50,text='',image=rotinas_btn_image, fg_color='transparent',font=('',100),command=lambda: conteudo_rotina.rotinas(conteudo_frame,janela),hover_color=cor_principal)
rotinas_btn.place(x=33,y=122)

#Botão de Pontuação (Mostra a pontuação do usuário)
pontos_btn = ctk.CTkButton(aba,10,50,text='',image=pontos_btn_image, fg_color='transparent',font=('',100),command=lambda:conteudo_pontuacao.pontuacao(conteudo_frame,janela),hover_color=cor_principal)
pontos_btn.place(x=33,y=210)

#Botão do Pomodoro pessoal
pomodoro_btn = ctk.CTkButton(aba,10,50,text='',image=pomodoro_btn_image, fg_color='transparent',font=('',100),command=lambda:conteudo_pomodoro.pomodoro(conteudo_frame,janela),hover_color=cor_principal)
pomodoro_btn.place(x=33,y=305)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Funções reutilizáveis para recarregar as notificações em todo o programa
def decidir_dia_atual():
    dia_atual = datetime.datetime.now().strftime("%A")
    return dia_atual


def notificar(titulo, mensagem):
        notificação = winotify.Notification(app_id='NeoTrax', title= titulo, msg= mensagem)
        notificação.show()           


def loop_diario(tela_principal):
        schedule.run_pending()
        tela_principal.after(1000, lambda: loop_diario(janela))


def recarregar_notifi():
    
    dia_atual = decidir_dia_atual()    
    dados = j.carregar_rotina(dia_atual)
    dados_de_ontem = j.carregar_rotina(ontem)
    
    remove_caracter_especial = str.maketrans('','',string.punctuation)
    
    #Aproveitando a atualização dos dados pra poder excluir as tarefas temporarias do dia anterior, sempre checando caso o usuário use o programa aberto direto, sem fechar
    for tarefa, info in list(dados_de_ontem.items()):
        if tarefa in dados_de_ontem:
            if info['tempo'] == 1:
                dados_de_ontem = j.carregar_rotina(ontem)
                del dados_de_ontem[tarefa]
                j.salvar_rotina(ontem, dados_de_ontem)
            
    for tarefa, info in list(dados.items()):
        try:
            
            hora_sistema = unidecode(hora).strip().lower().translate(remove_caracter_especial).replace(" ","")
            hora_salva_json = unidecode(info['hora_fim']).strip().lower().translate(remove_caracter_especial).replace(" ","")
                    
            schedule.every().day.at(info['hora_inicio']).do(lambda t= tarefa, i= info['desc']: notificar(f'Começando: {t}',i))    
            schedule.every().day.at(info['hora_fim']).do(lambda t= tarefa, i= info['desc']: notificar(f'Terminando: {t}',i))
            if info['tempo'] == 1 :
                if int(hora_sistema) > int(hora_salva_json):
                    dados = j.carregar_rotina(dia_atual)
                    del dados[tarefa]
                    j.salvar_rotina(dia_atual, dados)
                  
        except Exception as e:
            print('Notificação inexistente.',e)    

schedule.every(15).seconds.do(recarregar_notifi)            

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

loop_diario(janela)
janela.mainloop()