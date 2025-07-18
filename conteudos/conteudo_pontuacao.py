import customtkinter as ctk
import ntx_database as db

#Vai criar os gráficos de pontuação de cada dia da semana
def criar_gráfico(janela):
  
  def segunda():
    nome_dia = ctk.CTkLabel(janela,text='S',font=('',20),text_color='gray69')
    nome_dia.place(x=1,y=30)
    
    progress = ctk.CTkProgressBar(janela,800,50,corner_radius=19,fg_color='gray2',progress_color='yellow')
    progress.set(db.buscar_pontos_totais('Monday')/500)
    if db.buscar_pontos_totais('Monday') == 0:
      progress.configure(progress_color='gray2')
    progress.place(x=25, y= 18)
    
    return(db.buscar_pontos_totais('Monday'),db.buscar_pontos_totais('Monday','tarefa'))
    
  def terça():
    nome_dia = ctk.CTkLabel(janela,text='T',font=('',20),text_color='gray69')
    nome_dia.place(x=1,y=87)
    
    progress = ctk.CTkProgressBar(janela,800,50,corner_radius=19,fg_color='gray2',progress_color='yellow')
    progress.set(db.buscar_pontos_totais('Tuesday')/500)
    if db.buscar_pontos_totais('Tuesday') == 0:
      progress.configure(progress_color='gray2')
    progress.place(x=25, y= 75)
    
    return(db.buscar_pontos_totais('Tuesday'),db.buscar_pontos_totais('Tuesday','tarefa'))
    
  def quarta():
    nome_dia = ctk.CTkLabel(janela,text='Q',font=('',20),text_color='gray69')
    nome_dia.place(x=1,y=144)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19,fg_color='gray2',progress_color='yellow')
    progress.set(db.buscar_pontos_totais('Wednesday')/500)
    if db.buscar_pontos_totais('Wednesday') == 0:
      progress.configure(progress_color='gray2')  
    progress.place(x=25, y= 132)
    
    return(db.buscar_pontos_totais('Wednesday'),db.buscar_pontos_totais('Wednesday','tarefa'))
    
  def quinta():
    nome_dia = ctk.CTkLabel(janela,text='Q',font=('',20),text_color='gray69')
    nome_dia.place(x=1,y=201)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19,fg_color='gray2',progress_color='yellow')
    progress.set(db.buscar_pontos_totais('Thursday')/500)
    if db.buscar_pontos_totais('Thursday') == 0:
      progress.configure(progress_color='gray2') 
    progress.place(x=25, y= 189)
    
    return(db.buscar_pontos_totais('Thursday'),db.buscar_pontos_totais('Thursday','tarefa'))
    
  def sexta():
    nome_dia = ctk.CTkLabel(janela,text='S',font=('',20),text_color='gray69')
    nome_dia.place(x=1,y=258)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19,fg_color='gray2',progress_color='yellow')
    progress.set(db.buscar_pontos_totais('Friday')/500)
    if db.buscar_pontos_totais('Friday') == 0:
      progress.configure(progress_color='gray2') 
    progress.place(x=25, y= 246)
    
    return(db.buscar_pontos_totais('Friday'),db.buscar_pontos_totais('Friday','tarefa'))
    
  def sabado():
    nome_dia = ctk.CTkLabel(janela,text='S',font=('',20),text_color='gray69')
    nome_dia.place(x=1,y=315)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19,fg_color='gray2',progress_color='yellow')
    progress.set(db.buscar_pontos_totais('Saturday')/500)
    if db.buscar_pontos_totais('Saturday') == 0:
      progress.configure(progress_color='gray2') 
    progress.place(x=25, y= 303)
    
    return(db.buscar_pontos_totais('Saturday'),db.buscar_pontos_totais('Saturday','tarefa'))
    
  def domingo():
    nome_dia = ctk.CTkLabel(janela,text='D',font=('',20),text_color='gray69')
    nome_dia.place(x=1,y=372)
    
    progress = ctk.CTkProgressBar(janela,770,50,corner_radius=19,fg_color='gray2',progress_color='yellow')
    progress.set(db.buscar_pontos_totais('Sunday')/500)
    if db.buscar_pontos_totais('Sunday') == 0:
      progress.configure(progress_color='gray2') 
    progress.place(x=25, y= 360)
    
    return(db.buscar_pontos_totais('Sunday'),db.buscar_pontos_totais('Sunday','tarefa'))                      

#Comparador separado para a função seguinte
  def comparar_pontos():
    maior_ponto = 0.00
    maior_nome = 'N/A'
    maior_tarefa = 'N/A'
    try:
      segunda_ponto, segunda_tarefa = segunda()
      terça_ponto,terça_tarefa = terça()
      quarta_ponto, quarta_tarefa = quarta()
      quinta_ponto, quinta_tarefa = quinta()
      sexta_ponto, sexta_tarefa = sexta()
      sabado_ponto, sabado_tarefa = sabado()
      domingo_ponto, domingo_tarefa = domingo()
      #Eu não sabia como iterar esses nomes de forma simples, então fiz uma gambiarra funcional kkkkk
      
      if segunda_ponto > maior_ponto:
        maior_ponto = segunda_ponto
        maior_nome = 'Segunda - Feira'
        maior_tarefa = segunda_tarefa
      
      if terça_ponto > maior_ponto:
        maior_ponto = terça_ponto
        maior_nome = 'Terça - Feira'
        maior_tarefa = terça_tarefa
      
      if quarta_ponto > maior_ponto:
        maior_ponto = quarta_ponto
        maior_nome = 'Quarta - Feira'
        maior_tarefa = quarta_tarefa    
      
      if quinta_ponto > maior_ponto:
        maior_ponto = quinta_ponto
        maior_nome = 'Quinta - Feira'
        maior_tarefa = quinta_tarefa
      
      if sexta_ponto > maior_ponto:
        maior_ponto = sexta_ponto
        maior_nome = 'Sexta - Feira'
        maior_tarefa = sexta_tarefa
      
      if sabado_ponto > maior_ponto:
        maior_ponto = sabado_ponto
        maior_nome = 'Sábado'
        maior_tarefa = sabado_tarefa
      
      if domingo_ponto > maior_ponto:
        maior_ponto = domingo_ponto
        maior_nome = 'Domingo'
        maior_tarefa = domingo_tarefa
    except:
        maior_ponto = 0.00
        maior_nome = 'N/A'
        maior_tarefa = 'N/A'    
    return maior_nome,maior_ponto,maior_tarefa  
    

#Área em que vai mostrar o maior pontuador  
  def maior_pontuação():
    maior_pontuação_frame = ctk.CTkFrame(janela,850,200,fg_color='gray4')
    maior_pontuação_frame.place(x=1,y=429)
    
    maior_nome, maior_ponto,maior_tarefa = comparar_pontos()
    media_pontos = db.media_pontos()
  
    moldura = ctk.CTkFrame(maior_pontuação_frame,300,250,fg_color='transparent',border_color='gray2',border_width=12)
    moldura.place(x=570,y=-10)
    
    inicial_dia = ctk.CTkLabel(maior_pontuação_frame,width=1,height=1,text=maior_nome[0],font=('',140),text_color='yellow')
    inicial_dia.place(x=40,y=25)
    
    nome_dia_titulo = ctk.CTkLabel(maior_pontuação_frame,text='Dia em destaque:',font=('',15),text_color='gray69')
    nome_dia_titulo.place(x=200,y=45)
    nome_dia = ctk.CTkLabel(maior_pontuação_frame,text=maior_nome,font=('',15))
    nome_dia.place(x=319,y=45)
    
    pontos_totais_titulo = ctk.CTkLabel(maior_pontuação_frame,text='Pontos totais:',font=('',15),text_color='gray69')
    pontos_totais_titulo.place(x=200,y=90)
    pontos_totais = ctk.CTkLabel(maior_pontuação_frame,text=maior_ponto,fg_color='transparent',font=('',15))
    pontos_totais.place(x=300,y=90)

    if len(maior_tarefa) > 20:
      maior_tarefa = f'{maior_tarefa[:20]}...'
    
    tarefa_mais_feita_titulo = ctk.CTkLabel(maior_pontuação_frame,text='Tarefa mais pontuada do dia:',font=('',15),text_color='gray69')
    tarefa_mais_feita_titulo.place(x=200,y=135)    
    tarefa_mais_feita = ctk.CTkLabel(maior_pontuação_frame,text=maior_tarefa,fg_color='transparent',font=('',15))
    tarefa_mais_feita.place(x=395,y=135)   

    media_titulo = ctk.CTkLabel(maior_pontuação_frame,text='Média semanal',font=('',25),text_color='gray69')
    media_titulo.place(x=630,y=14)        
    media = ctk.CTkLabel(maior_pontuação_frame,text=media_pontos,fg_color='transparent',font=('',70))
    media.place(x=625,y=70)
      
  
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



 
 
  

