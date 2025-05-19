import customtkinter as ctk

#Tela de Configurações
def config(jnl):
 for widget in jnl.winfo_children():
    widget.destroy()
 title = ctk.CTkLabel(jnl,text='CONFIGURAÇÕES',font=('Cascadia Code', 20))
 title.pack()
   


#Tela de Ajuda
def ajuda(jnl):
 for widget in jnl.winfo_children():
    widget.destroy()
 title = ctk.CTkLabel(jnl,text='TESTE')
 title.pack()    