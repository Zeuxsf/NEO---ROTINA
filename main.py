#NEOTRAX (Nome a decidir)
import customtkinter as ctk
import conteudo as btn
from PIL import Image

#Configurações da Janela Principal
janela = ctk.CTk()
janela.geometry('1000x700')
janela.resizable(False,False)
janela.title('Neo-Rotina')
ctk.set_appearance_mode('System')

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
aba = ctk.CTkFrame(janela,120,1211)
aba.place(x=1,y=0)

#Botões:

#Botão de Configuração (Configurações do programa)
configbtn = ctk.CTkButton(aba,10,10,text='',command=lambda: btn.config(conteudo_frame),image=configbtn_image,fg_color='transparent')
configbtn.place(x= 70,y=650)

#Botão de Ajuda (Ajuda o usuário a navegar pelo Programa, e também, mostra os créditos (autor, etc))
ajudabtn = ctk.CTkButton(aba,25,10,text='',command=lambda: btn.ajuda(conteudo_frame),image= ajudabtn_image,fg_color='transparent')
ajudabtn.place(x=10,y=650)

#Botão Minha Rotina (Rotina do dia Atual)
rotina_atualbtn = ctk.CTkButton(aba,10,50,text='',image=rotina_atualbtn_image, fg_color='transparent',font=('',100), command=lambda: btn.rotina_atual(conteudo_frame,janela))
rotina_atualbtn.place(x=33,y=35)

#Botão Rotinas (Todas as rotinas)
rotinas_btn = ctk.CTkButton(aba,10,50,text='',image=rotinas_btn_image, fg_color='transparent',font=('',100),command=lambda: btn.rotinas(conteudo_frame,janela))
rotinas_btn.place(x=33,y=122)

#Botão de Pontuação (Mostra a pontuação do usuário)
pontos_btn = ctk.CTkButton(aba,10,50,text='',image=pontos_btn_image, fg_color='transparent',font=('',100),command=lambda:btn.pontuacao(conteudo_frame))
pontos_btn.place(x=33,y=210)

#Botão do Pomodoro pessoal
pomodoro_btn = ctk.CTkButton(aba,10,50,text='',image=pomodoro_btn_image, fg_color='transparent',font=('',100),command=lambda:btn.pomodoro(conteudo_frame))
pomodoro_btn.place(x=33,y=305)



janela.mainloop()