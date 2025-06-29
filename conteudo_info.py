import customtkinter as ctk

#Tela de Ajuda
def info(jnl,tela_principal):
 for widget in jnl.winfo_children():
    widget.destroy()

 tela_principal.geometry('1000x650')    
 title = ctk.CTkLabel(jnl,text='EM OBRA',font = ('',120))
 title.pack()    
