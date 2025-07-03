import customtkinter as ctk
from winotify import Notification

#Vai notificar o usuário quando a contagem acabar
def notificar(titulo, mensagem):
   notificação = Notification(app_id='NeoTrax', title=titulo, msg=mensagem)
   notificação.show()

#Vai iniciar a contagem
#(o parâmetro "identificador" vai dizer se é o contador de estudo ou de descanso)
def iniciar(minutos, identificador, iniciar_btn, descanso_btn, cronometro, tela_principal, janela):
  
   segundos = minutos * 60
   pausado = False
         
   descanso_btn.place_forget()
   iniciar_btn.place_forget()
   
   def atualizar(taxa_de_atualização=1):
      
    nonlocal segundos
    
    if pausado:
       return
    
    try:
         if segundos >= 0:      
            mins = segundos // 60
            segs = segundos % 60  
            cronometro.configure(text=f'{mins:02d}:{segs:02d}')
            segundos -= taxa_de_atualização
            tela_principal.after(1000,atualizar)
         else:
            iniciar_btn.place(x=340,y=380)
            descanso_btn.place(x=430,y=380)
            pause_btn.destroy()       
            
         if segundos == 0:
            iniciar_btn.place(x=340,y=380)
            descanso_btn.place(x=430,y=380)
            pause_btn.destroy() 
            
            if identificador == 0:
              notificar('Temporizador Zerado!', 'Hora de ter uma PAUSA!')
            
            else: 
               notificar('Temporizador Zerado!', 'Hora de voltar pra AÇÃO!')
    except:
         print('Contador Zerado')               
   
   #Função para pausar a contagem
   def pause():
      nonlocal pausado
      pausado = not pausado
      troca_texto = 'Continuar' if pausado else 'Pausar'
         
      pause_btn.configure(text = troca_texto)
      
      if not pausado:
       atualizar()
                  
   pause_btn = ctk.CTkButton(janela,50,50,text='Pausar', text_color='white', command=pause)
   pause_btn.place(x=380,y=380)      

   atualizar()
         
#É a aba que vai mostrar o pomodoro na tela
def pomodoro(janela,tela_principal):
 for widget in janela.winfo_children():
    widget.destroy()

 tela_principal.geometry('1000x650')    

 cronometro = ctk.CTkLabel(janela,20,20,text='00:00',text_color='white',font=('Franklin Gothic',110))
 cronometro.place(x=298,y=98)
 
 iniciar_btn = ctk.CTkButton(janela,50,50,text='Começar', text_color='white', command= lambda: iniciar(25, 0,iniciar_btn,descanso_btn,cronometro, tela_principal, janela) )
 iniciar_btn.place(x=340,y=380)

 descanso_btn = ctk.CTkButton(janela,50,50,text='Descansar', text_color='white', command= lambda: iniciar(10, 1,iniciar_btn,   descanso_btn,cronometro, tela_principal, janela) )
 descanso_btn.place(x=430,y=380)
 
 


