import customtkinter as ctk

#Tela de Configurações
def config(jnl,tela_principal):
 for widget in jnl.winfo_children():
    widget.destroy()

 tela_principal.geometry('1000x650')    
 title = ctk.CTkLabel(jnl,text='CONFIGURAÇÕES',font=('Cascadia Code', 20))
 title.pack()
   