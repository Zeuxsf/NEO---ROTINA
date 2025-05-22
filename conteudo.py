import customtkinter as ctk

#Sistema de frames para cada dia da semana, para auxiliar na organização
def dias(tela,tela_principal,mostrar=False):
  
  def segunda():
   if 'seg' in mostrar:
      segunda_frame = ctk.CTkScrollableFrame(tela,820,651)
      segunda_frame.pack(pady = 5)
      
      title = ctk.CTkLabel(segunda_frame,text='Segunda', font=('',35))
      title.pack(pady=15)

      def addtarefatela():
        tarefatela = ctk.CTkToplevel(tela_principal)
        label = ctk.CTkLabel(tarefatela,text='oi').pack()  

      def addtarefa():
        tarefa = ctk.CTkFrame(segunda_frame,720,100,border_color='snow2',border_width=1)
        tarefa.pack(pady=5)

      add_tarefa_btn = ctk.CTkButton(segunda_frame,text='+',width=20,height=20,command=addtarefatela)
      add_tarefa_btn.place(x=490,y=30)

  def terça():
   if 'ter' in mostrar:
      terça_frame = ctk.CTkScrollableFrame(tela,820,651)
      terça_frame.pack(pady = 5)
  
  def quarta():
   if 'qua' in mostrar:
      quarta_frame = ctk.CTkScrollableFrame(tela,820,651)
      quarta_frame.pack(pady = 5)
  
  def quinta():
   if 'qui' in mostrar:
      quinta_frame = ctk.CTkScrollableFrame(tela,820,651)
      quinta_frame.pack(pady = 5)
  
  def sexta():
   if 'sex' in mostrar:
      sexta_frame = ctk.CTkScrollableFrame(tela,820,651)
      sexta_frame.pack(pady = 5)
  
  def sabado():
   if 'sab' in mostrar:
      sabado_frame = ctk.CTkScrollableFrame(tela,820,651)
      sabado_frame.pack(pady = 5)
  
  def domingo():
   if 'dom' in mostrar:
      domingo_frame = ctk.CTkScrollableFrame(tela,820,651)
      domingo_frame.pack(pady = 5)

  segunda()
  terça()
  quarta()
  quinta()
  sexta()
  sabado()
  domingo() 


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


def rotina_atual(jnl,tela_principal):
 for widget in jnl.winfo_children():
    widget.destroy()

 dias(jnl,tela_principal,'seg')    


def rotinas(jnl,tela_principal):
 for widget in jnl.winfo_children():
    widget.destroy()

 dias(jnl,tela_principal,'seg,ter,qua,qui,sex,sab,dom')


def pontuacao(jnl):
 for widget in jnl.winfo_children():
    widget.destroy()
 title = ctk.CTkLabel(jnl,text='TESTE')
 title.pack()     


def pomodoro(jnl):
 for widget in jnl.winfo_children():
    widget.destroy()
 title = ctk.CTkLabel(jnl,text='TESTE')
 title.pack()    


