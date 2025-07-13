import customtkinter as ctk
from PIL import Image
import conteudo_rotina as r
import conteudo_config as j

pause_btn_image = ctk.CTkImage(Image.open('imagens/pausa.png'),size=(40,40))
play_btn_image = ctk.CTkImage(Image.open('imagens/play.png'),size=(40,40))
descanso_btn_image = ctk.CTkImage(Image.open('imagens/descanso.png'),size=(40,40))
iniciar_btn_image = ctk.CTkImage(Image.open('imagens/começar.png'),size=(40,40))
reiniciar_btn_image = ctk.CTkImage(Image.open('imagens/reiniciar.png'),size=(40,40))

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
            descanso_btn.place(x=465,y=380)
            pause_btn.destroy()
            reiniciar_btn.destroy()       
            
         if segundos == 0:
            iniciar_btn.place(x=340,y=380)
            descanso_btn.place(x=465,y=380)
            pause_btn.destroy()
            reiniciar_btn.destroy() 
            
            usuario = j.carregar_configs()['usuario']
            if identificador == 0:
              r.notificar('Temporizador Zerado!', f'Hora de ter uma PAUSA {usuario}!','pomodoro')
            
            else: 
               r.notificar('Temporizador Zerado!', f'Hora de você voltar pra AÇÃO {usuario}!','pomodoro')
    except:
         print('Contador Zerado')               
   
   #Função para pausar a contagem
   def pause():
      nonlocal pausado
      pausado = not pausado
      troca_img = play_btn_image if pausado else pause_btn_image
         
      pause_btn.configure(image = troca_img)
      
      if not pausado:
       atualizar()
                  
   pause_btn = ctk.CTkButton(janela,50,50,text='', image=pause_btn_image,fg_color='transparent',hover_color='gray2', command=pause)
   pause_btn.place(x=380,y=380)
   reiniciar_btn = ctk.CTkButton(janela,50,50,text='', image=reiniciar_btn_image,fg_color='transparent',hover_color='gray2', command=lambda:pomodoro(janela,tela_principal))
   reiniciar_btn.place(x=430,y=380)      

   atualizar()
         
#É a aba que vai mostrar o pomodoro na tela
def pomodoro(janela,tela_principal):
 for widget in janela.winfo_children():
    widget.destroy()

 tela_principal.geometry('1000x650')    

 cronometro = ctk.CTkLabel(janela,20,20,text='00:00',text_color='white',font=('Franklin Gothic',200))
 cronometro.place(x=180,y=98)
 
 dados = j.carregar_configs()
 
 iniciar_btn = ctk.CTkButton(janela,50,50,text='', image=iniciar_btn_image,fg_color='transparent',hover_color='gray2', command= lambda: iniciar(int(dados['p_tempo']), 0,iniciar_btn,descanso_btn,cronometro, tela_principal, janela) )
 iniciar_btn.place(x=340,y=380)

 descanso_btn = ctk.CTkButton(janela,50,50,text='', image=descanso_btn_image,fg_color='transparent',hover_color='gray2', command= lambda: iniciar(int(dados['p_descanso']), 1,iniciar_btn,   descanso_btn,cronometro, tela_principal, janela) )
 descanso_btn.place(x=465,y=380)
 
 


