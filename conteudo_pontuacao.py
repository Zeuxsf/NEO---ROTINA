import customtkinter as ctk
import ntx_database as db

#Vai criar os gráficos de pontuação de cada dia da semana
def criar_gráfico(janela):
  
  def segunda():
    titulo = ctk.CTkLabel(janela,text='S',font=('',20))
    titulo.place(x=1,y=30)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19)
    progress.set(db.buscar_pontos_totais('Monday'))
    progress.place(x=25, y= 18)
    
    pontos_totais = ctk.CTkLabel(janela,text=db.buscar_pontos_totais('Monday'),fg_color='transparent',font=('',30))
    pontos_totais.place(x=800,y=30)
    return(db.buscar_pontos_totais('Monday'))
    
  def terça():
    titulo = ctk.CTkLabel(janela,text='T',font=('',20))
    titulo.place(x=1,y=87)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19)
    progress.set(db.buscar_pontos_totais('Tuesday'))
    progress.place(x=25, y= 75)
    
    pontos_totais = ctk.CTkLabel(janela,text=db.buscar_pontos_totais('Tuesday'),fg_color='transparent',font=('',30))
    pontos_totais.place(x=800,y=87)
    return(db.buscar_pontos_totais('Tuesday'))
    
  def quarta():
    titulo = ctk.CTkLabel(janela,text='Q',font=('',20))
    titulo.place(x=1,y=144)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19)
    progress.set(db.buscar_pontos_totais('Wednesday'))
    progress.place(x=25, y= 132)
    
    pontos_totais = ctk.CTkLabel(janela,text=db.buscar_pontos_totais('Wednesday'),fg_color='transparent',font=('',30))
    pontos_totais.place(x=800,y=144)
    return(db.buscar_pontos_totais('Wednesday'))
    
  def quinta():
    titulo = ctk.CTkLabel(janela,text='Q',font=('',20))
    titulo.place(x=1,y=201)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19)
    progress.set(db.buscar_pontos_totais('Thursday'))
    progress.place(x=25, y= 189)
    
    pontos_totais = ctk.CTkLabel(janela,text=db.buscar_pontos_totais('Thursday'),fg_color='transparent',font=('',30))
    pontos_totais.place(x=800,y=201)
    return(db.buscar_pontos_totais('Thursday'))
    
  def sexta():
    titulo = ctk.CTkLabel(janela,text='S',font=('',20))
    titulo.place(x=1,y=258)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19)
    progress.set(db.buscar_pontos_totais('Friday'))
    progress.place(x=25, y= 246)
    
    pontos_totais = ctk.CTkLabel(janela,text=db.buscar_pontos_totais('Friday'),fg_color='transparent',font=('',30))
    pontos_totais.place(x=800,y=258)
    return(db.buscar_pontos_totais('Friday'))
    
  def sabado():
    titulo = ctk.CTkLabel(janela,text='S',font=('',20))
    titulo.place(x=1,y=315)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19)
    progress.set(db.buscar_pontos_totais('Saturday'))
    progress.place(x=25, y= 303)
    
    pontos_totais = ctk.CTkLabel(janela,text=db.buscar_pontos_totais('Saturday'),fg_color='transparent',font=('',30))
    pontos_totais.place(x=800,y=315)
    return(db.buscar_pontos_totais('Saturday'))
    
  def domingo():
    titulo = ctk.CTkLabel(janela,text='D',font=('',20))
    titulo.place(x=1,y=372)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19)
    progress.set(db.buscar_pontos_totais('Sunday'))
    progress.place(x=25, y= 360)
    
    pontos_totais = ctk.CTkLabel(janela,text=db.buscar_pontos_totais('Sunday'),fg_color='transparent',font=('',30))
    pontos_totais.place(x=800,y=372)
    return(db.buscar_pontos_totais('Sunday'))                      

#Comparador separado para a função seguinte
  def comparar_pontos():
    maior_ponto = 0
    maior_nome = ''
    
    segunda_ponto = segunda()
    terça_ponto = terça()
    quarta_ponto = quarta()
    quinta_ponto = quinta()
    sexta_ponto = sexta()
    sabado_ponto = sabado()
    domingo_ponto = domingo()
    #Eu não sabia como iterar esses números de forma simples, então fiz uma gambiarra funcional kkkkk
    if segunda_ponto > maior_ponto:
      maior_ponto = segunda_ponto
      maior_nome = 'Segunda'
    if terça_ponto > maior_ponto:
      maior_ponto = terça_ponto
      maior_nome = 'Terça'
    if quarta_ponto > maior_ponto:
      maior_ponto = quarta_ponto
      maior_nome = 'Quarta'    
    if quinta_ponto > maior_ponto:
      maior_ponto = quinta_ponto
      maior_nome = 'Quinta'
    if sexta_ponto > maior_ponto:
      maior_ponto = sexta_ponto
      maior_nome = 'Sexta'
    if sabado_ponto > maior_ponto:
      maior_ponto = sabado_ponto
      maior_nome = 'Sábado'
    if domingo_ponto > maior_ponto:
      maior_ponto = domingo_ponto
      maior_nome = 'Domingo'
    return maior_nome,maior_ponto  
    

#Área em que vai mostrar o maior pontuador  
  def maior_pontuação():
    maior_pontuação_frame = ctk.CTkFrame(janela,850,200)
    maior_pontuação_frame.place(x=1,y=429)
    
    maior_nome, maior_ponto = comparar_pontos()
                    
    titulo = ctk.CTkLabel(maior_pontuação_frame,text='Dia em Destaque',font=('',27))
    titulo.place(x=1,y=7)
    
    nome_dia = ctk.CTkLabel(maior_pontuação_frame,text=maior_nome,font=('',27))
    nome_dia.place(x=1,y=35)
    
    
    pontos_totais = ctk.CTkLabel(maior_pontuação_frame,text=maior_ponto,fg_color='transparent',font=('',30))
    pontos_totais.place(x=735,y=7)    
  
  segunda()
  terça()
  quarta()
  quinta()
  sexta()
  sabado()
  domingo()
  maior_pontuação()  
    

def pontuacao(janela,tela_principal,dia_atual):
 for widget in janela.winfo_children():
    widget.destroy()  
 tela_principal.geometry('1000x650')   
 criar_gráfico(janela)



 
 
  

