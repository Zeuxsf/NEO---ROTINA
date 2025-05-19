#NEOTRAX (Nome a decidir)
import customtkinter as ctk
import conteudo as btn
from PIL import Image

#Configurações da Janela Principal
janela = ctk.CTk()
janela.geometry('1000x700')
janela.resizable(False,False)
janela.title('Neo-Rotina')
#Uma tela scrolável, pro programa ter liberdade de crescer
conteudo_frame = ctk.CTkScrollableFrame(janela,814,670,fg_color='transparent')
conteudo_frame.place(x=159,y=10)

#Imagens usadas no programa:
configbtn_image = ctk.CTkImage(Image.open('imagens/cfg.png'))
ajudabtn_image = ctk.CTkImage(Image.open('imagens/inf.png'))

#Configurações da Aba Lateral, a Navegação do programa
aba = ctk.CTkFrame(janela,150,1211)
aba.place(x=1,y=0)

#Botões:

#Botão de Configuração
configbtn = ctk.CTkButton(aba,10,10,text='',command=lambda: btn.config(conteudo_frame),image=configbtn_image,fg_color='transparent')
configbtn.place(x= 80,y=650)
#Botão de Ajuda
ajudabtn = ctk.CTkButton(aba,25,10,text='',command=lambda: btn.ajuda(conteudo_frame),image= ajudabtn_image,fg_color='transparent')
ajudabtn.place(x=20,y=650)
#Botão de 




janela.mainloop()