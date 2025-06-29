import customtkinter as ctk
import conteudo_rotina as conteudo_rotina 
import conteudo_config as conteudo_config
import conteudo_info as conteudo_info
import conteudo_pomodoro as conteudo_pomodoro
import conteudo_pontuacao as conteudo_pontuacao
from PIL import Image
import datetime
import winotify
import schedule
import ntx_database as db

#Lógica que usa lib datetime para pegar os dias e horários e transforma eles em string
hoje = datetime.datetime.now()
ontem = hoje - datetime.timedelta(days=1)
ontem = ontem.strftime("%A")
hora = hoje.strftime("%H:%M")

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
configbtn = ctk.CTkButton(aba,10,10,text='',command=lambda: conteudo_config.config(conteudo_frame,janela),image=configbtn_image,fg_color='transparent',hover_color='dodgerblue')
configbtn.place(x= 70,y=600)

#Botão de Ajuda (Ajuda o usuário a navegar pelo Programa, e também, mostra os créditos (autor, etc))
ajudabtn = ctk.CTkButton(aba,25,10,text='',command=lambda: conteudo_info.info(conteudo_frame,janela),image= ajudabtn_image,fg_color='transparent',hover_color='dodgerblue')
ajudabtn.place(x=10,y=600)

#Botão Minha Rotina (Rotina do dia Atual)
rotina_atualbtn = ctk.CTkButton(aba,10,50,text='',image=rotina_atualbtn_image, fg_color='transparent',font=('',100), command=lambda: conteudo_rotina.rotina_atual(conteudo_frame,janela),hover_color='dodgerblue')
rotina_atualbtn.place(x=33,y=35)

#Botão Rotinas (Todas as rotinas)
rotinas_btn = ctk.CTkButton(aba,10,50,text='',image=rotinas_btn_image, fg_color='transparent',font=('',100),command=lambda: conteudo_rotina.rotinas(conteudo_frame,janela),hover_color='dodgerblue')
rotinas_btn.place(x=33,y=122)

#Botão de Pontuação (Mostra a pontuação do usuário)
pontos_btn = ctk.CTkButton(aba,10,50,text='',image=pontos_btn_image, fg_color='transparent',font=('',100),command=lambda:conteudo_pontuacao.pontuacao(conteudo_frame,janela),hover_color='dodgerblue')
pontos_btn.place(x=33,y=210)

#Botão do Pomodoro pessoal
pomodoro_btn = ctk.CTkButton(aba,10,50,text='',image=pomodoro_btn_image, fg_color='transparent',font=('',100),command=lambda:conteudo_pomodoro.pomodoro(conteudo_frame,janela),hover_color='dodgerblue')
pomodoro_btn.place(x=33,y=305)


#Funções que vão verificar o dia e horário para mostrar as notificações das tarefas
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
    dados = db.carregar_rotina(dia_atual)
    
    #Aproveitando o sistema de verificação das notificações para poder excluir as tarefas temporarias do dia anterior, sempre checando caso o usuário use o programa aberto direto, sem fechar
    for linha in dados:
        if ontem == linha[3]:
            db.cursor.execute('''DELETE FROM trax WHERE temporario = ? dia = ?''',('1',ontem))
            db.conexao.commit()
            
    for linha in dados:
        try:        
            schedule.every().day.at(linha[4]).do(lambda t= linha[1], i= linha[2]: notificar(f'Começando: {t}',i))    
            schedule.every().day.at(linha[5]).do(lambda t= linha[1], i= linha[2]: notificar(f'Terminando: {t}',i))
        except Exception as e:
            print('Notificação inexistente.',e)    

schedule.every(15).seconds.do(recarregar_notifi)            
loop_diario(janela)

#Encerrando programa e banco de dados
janela.mainloop()
db.encerrar_conexao()