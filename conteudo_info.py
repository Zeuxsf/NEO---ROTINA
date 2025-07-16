import customtkinter as ctk
from PIL import Image
import conteudo_config as j
import ntx_database as db

#imagens:
creditos_btn_image = ctk.CTkImage(Image.open(db.caminho('imagens/prosseguir.png')), size=(30,30))
informacoes_btn_image = ctk.CTkImage(Image.open(db.caminho('imagens/voltar.png')), size=(30,30))

def creditos(janela,tela_principal):
 for widget in janela.winfo_children():
    widget.destroy()

 tela_principal.geometry('1000x650')    
 titulo = ctk.CTkLabel(janela,text='Créditos',font = ('',30))
 titulo.place(x=375,y=10)
 
 texto = ctk.CTkLabel(janela,text='''Imagens/Ícones utilizados no programa:

Logo oficial do NeoTrax: R! Marketing (Robson França)

Aba Pomodoro: Fajrul Fitrianto
Aba Rotinas Gerais: Freepik
Aba Dia Atual: KP Arts
Aba Pontuação: Dzihab
Aba Configurações: Freepik
Aba Informações: Freepik
Botão de Editar: feen
Botão de Excluir: inkubators
Botão de Encerrar o Dia: nangicon
Botão de Pause: slidicon
Botão de Play: Freepik
Timer de Descanso: icon_small
Timer de Produtividade: Arkinasi
Botão de Reset (Pomodoro): Artmuhammed
Setas de prosseguir e voltar: Roundicons


Agradecimentos especiais a:
Ana Clara, por todo suporte moral, emocional e por sempre me incentivar nos momentos em que mais precisei. 💛

Criador e idealizador do programa:
Alexandre S. de França

📩 Contato/Pix para doação:
alexandresf8105@gmail.com'''
   ,font = ('',15),wraplength=800)
 texto.place(x=56,y=100)
 
 informacoes_btn = ctk.CTkButton(janela,image=informacoes_btn_image,text='',fg_color='transparent',hover_color='gray2',command=lambda:info(janela,tela_principal))
 informacoes_btn.place(x=358,y=50) 
   

#Tela de Ajuda
def info(janela,tela_principal):
 for widget in janela.winfo_children():
    widget.destroy()

 tela_principal.geometry('1000x650')    
 titulo = ctk.CTkLabel(janela,text='Informações',font = ('',30))
 titulo.place(x=350,y=10)
 
 usuario = j.carregar_configs()['usuario']
 texto = ctk.CTkLabel(janela,text=f'''👋 Seja bem-vindo(a), {usuario}, à sua nova trilha!
   O NeoTrax foi criado para te ajudar a organizar sua rotina com ferramentas que vão te tornar muito mais produtivo do que antes!
   
   🔹 Aba de Tarefas do Dia
   Exibe as tarefas que você se propôs a realizar no dia atual. É a única aba onde você pode pontuar suas tarefas, após clicar no botão "Encerrar Dia".
   
   🔹 Aba de Rotinas Gerais
   Permite visualizar e ajustar suas rotinas sem precisar esperar os dias passarem. Você pode marcar como feitas apenas as tarefas do dia atual, mas não pode encerrar o dia por aqui.
   
   🔹 Aba de Pontuação
   Um quadro para você acompanhar seu desempenho ao longo da semana. Mostra qual é o seu dia mais produtivo com base na pontuação!
   Lembre-se: tarefas temporárias somem junto com seus pontos. Apenas as tarefas fixas contam pontos permanentes.
   
   🔹 Aba do Pomodoro
   O Pomodoro é uma técnica muito utilizada para melhorar foco e rendimento nos estudos e no trabalho. Ela consiste em ciclos de produtividade intercalados com pausas.
   Aqui no NeoTrax, o timer é totalmente customizável, e você pode ajustá-lo na aba de Configurações.

   🛠️ Funcionalidades adicionais do NeoTrax:

   - Iniciar com o sistema: ative essa opção na aba de configurações para abrir o NeoTrax automaticamente com seu Windows. Ideal para quem pretende usar todos os dias.
   - Funcionamento em segundo plano: ao minimizar o programa, ele vai direto para a bandeja do sistema (perto do relógio), sem atrapalhar sua área de trabalho.
   - Notificações: receba alertas sobre tarefas pendentes e ciclos do Pomodoro, para manter o foco sem precisar ficar conferindo manualmente.'''
   ,font = ('',15),wraplength=800)
 texto.place(x=23,y=100)
 
 creditos_btn = ctk.CTkButton(janela,image=creditos_btn_image,text='',fg_color='transparent',hover_color='gray2',command=lambda:creditos(janela,tela_principal))
 creditos_btn.place(x=358,y=50) 

