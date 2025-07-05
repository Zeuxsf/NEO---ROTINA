import customtkinter as ctk
import ntx_database as db
import schedule
import datetime

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sistema de frames para cada dia da semana, para auxiliar na organização
def dias(janela, tela_principal, mostrar=False,aba_atual=False):

    def segunda():
        if 'Monday' in mostrar:
            segunda_frame = ctk.CTkScrollableFrame(janela, 842, 610,fg_color='gray4',scrollbar_button_color='gray23',scrollbar_button_hover_color='gray9')
            segunda_frame.pack(pady=5)

            title = ctk.CTkLabel(segunda_frame, text="Segunda", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton(segunda_frame,text="+",text_color='black',fg_color='yellow',hover_color='gold3',width=20,height=20,
                command=lambda: criador_de_tarefas(segunda_frame, tela_principal,'Monday',aba_atual),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(segunda_frame,tela_principal,'Monday',aba_atual)

    def terça():
        if 'Tuesday' in mostrar:
            terça_frame = ctk.CTkScrollableFrame(janela, 842, 610,fg_color='gray4',scrollbar_button_color='gray23',scrollbar_button_hover_color='gray9')
            terça_frame.pack(pady=5)

            title = ctk.CTkLabel(terça_frame, text="Terça", font=("", 35))
            title.pack(pady=15)
            
            add_tarefa_btn = ctk.CTkButton(  terça_frame,text="+",text_color='black',fg_color='yellow',hover_color='gold3',width=20,height=20,
                command=lambda: criador_de_tarefas(terça_frame, tela_principal,'Tuesday',aba_atual),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(terça_frame,tela_principal,'Tuesday',aba_atual)

    def quarta():
        if "Wednesday" in mostrar:
            quarta_frame = ctk.CTkScrollableFrame(janela, 842, 610,fg_color='gray4',scrollbar_button_color='gray23',scrollbar_button_hover_color='gray9')
            quarta_frame.pack(pady=5)

            title = ctk.CTkLabel(quarta_frame, text="Quarta", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton( quarta_frame,text="+",text_color='black',fg_color='yellow',hover_color='gold3',width=20,height=20,
                command=lambda: criador_de_tarefas(quarta_frame, tela_principal,'Wednesday',aba_atual),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(quarta_frame,tela_principal,'Wednesday',aba_atual)

    def quinta():
        if "Thursday" in mostrar:
            quinta_frame = ctk.CTkScrollableFrame(janela, 842, 610,fg_color='gray4',scrollbar_button_color='gray23',scrollbar_button_hover_color='gray9')
            quinta_frame.pack(pady=5)
            

            title = ctk.CTkLabel(quinta_frame, text="Quinta", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton( quinta_frame,text="+",text_color='black',fg_color='yellow',hover_color='gold3',width=20,height=20,
                command=lambda: criador_de_tarefas(quinta_frame, tela_principal,'Thursday',aba_atual),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(quinta_frame,tela_principal,'Thursday',aba_atual)            

    def sexta():
        if "Friday" in mostrar:
            sexta_frame = ctk.CTkScrollableFrame(janela, 842, 610,fg_color='gray4',scrollbar_button_color='gray23',scrollbar_button_hover_color='gray9')
            sexta_frame.pack(pady=5)

            title = ctk.CTkLabel(sexta_frame, text="Sexta", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton( sexta_frame,text="+",text_color='black',fg_color='yellow',hover_color='gold3',width=20,height=20,
                command=lambda: criador_de_tarefas(sexta_frame, tela_principal,'Friday',aba_atual),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(sexta_frame,tela_principal,'Friday',aba_atual)            

    def sabado():
        if "Saturday" in mostrar:
            sabado_frame = ctk.CTkScrollableFrame(janela, 842, 610,fg_color='gray4',scrollbar_button_color='gray23',scrollbar_button_hover_color='gray9')
            sabado_frame.pack(pady=5)

            title = ctk.CTkLabel(sabado_frame, text="Sábado", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton( sabado_frame,text="+",text_color='black',fg_color='yellow',hover_color='gold3',width=20,height=20,
                command=lambda: criador_de_tarefas(sabado_frame, tela_principal,'Saturday',aba_atual),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(sabado_frame,tela_principal,'Saturday',aba_atual)            

    def domingo():
        if "Sunday" in mostrar:
            domingo_frame = ctk.CTkScrollableFrame(janela, 842, 610,fg_color='gray4',scrollbar_button_color='gray23',scrollbar_button_hover_color='gray9')
            domingo_frame.pack(pady=5)
            

            title = ctk.CTkLabel(domingo_frame, text="Domingo", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton(domingo_frame,text="+",text_color='black',fg_color='yellow',hover_color='gold3',width=20,height=20,
                command=lambda: criador_de_tarefas(domingo_frame, tela_principal,'Sunday',aba_atual),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(domingo_frame,tela_principal,'Sunday',aba_atual)            

    segunda()
    terça()
    quarta()
    quinta()
    sexta()
    sabado()
    domingo()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Aba em que o usuário vai preencher as informações da tarefa
def criador_de_tarefas(frame_dia, tela_principal,dia,aba_atual=False):

    tela_principal.geometry("1250x650")

    tarefatela = ctk.CTkFrame(
        tela_principal, 245, 635, border_color='yellow', border_width=1,fg_color='gray4')
    tarefatela.place(x=1000, y=10)

    nome_da_tarefa = ctk.CTkEntry(
        tarefatela, 225, 25, placeholder_text="Título da Tarefa...",fg_color='gray9',border_color='gray4')
    nome_da_tarefa.place(x=10, y=7)

    desc_da_tarefa = ctk.CTkTextbox(tarefatela, 225, 200,fg_color='gray9')
    desc_da_tarefa.place(x=10, y=39)
    desc_da_tarefa.insert(index="0.0", text="Descrição da Tarefa...")

    hora_texto = ctk.CTkLabel(
        tarefatela, text="Hora de ínicio.        Hora de encerramento."
    )
    hora_texto.place(x=7, y=239)

    hora_inicio = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="11",fg_color='gray4')
    min_inicio = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="59",fg_color='gray4')
    hora_inicio.place(x=7, y=265)
    min_inicio.place(x=47, y=265)

    hora_fim = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="23",fg_color='gray4')
    min_fim = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="59",fg_color='gray4')
    hora_fim.place(x=140, y=265)
    min_fim.place(x=180, y=265)

    variavel_escolha = ctk.IntVar(value=1)

    temporario_escolha = ctk.CTkRadioButton(
        tarefatela, text="Temporária", variable=variavel_escolha, value=1,fg_color='deepskyblue2',hover_color='deepskyblue3'
    )
    fixo_escolha = ctk.CTkRadioButton(
        tarefatela, text="Fixa", variable=variavel_escolha, value=2,fg_color='yellow',hover_color='gold3'
    )
    temporario_escolha.place(x=15, y=310)
    fixo_escolha.place(x=130, y=310)

    salvar_btn = ctk.CTkButton(
        tarefatela,
        text="SALVAR",
        fg_color='yellow',
        hover_color='gold3',
        text_color='black',
        width=225,
        height=25,
        command=lambda: adicionar_tarefa(
            frame_dia,
            tela_principal,
            nome_da_tarefa.get(),
            desc_da_tarefa.get("1.0", "end"),
            variavel_escolha.get(),
            hora_inicio.get(),
            min_inicio.get(),
            hora_fim.get(),
            min_fim.get(),
            dia,
            tarefatela.destroy(),
            carregando=False,
            aba_atual=aba_atual
        ),
    )
    salvar_btn.place(x=10, y=600)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Carregador de tarefas: vai carregar as informações salvas no banco de dados pra função que adiciona a tarefa na tela 
def iniciar_tela_rotina(frame_dia,tela_principal,dia,aba_atual=False):
    dados = db.carregar_rotina(dia)
    
    for linha in dados:
        if linha[3] == dia:
            adicionar_tarefa(frame_dia=frame_dia,
                         nome_da_tarefa=linha[1],
                         desc_da_tarefa=linha[2],
                         temp_ou_fix=linha[6],
                         hora_inicio=linha[4],
                         hora_fim=linha[5],
                         dia_semana=linha[3],
                         check_state = linha[7],
                         tela_principal=tela_principal,
                         carregando = True,
                         aba_atual=aba_atual
                         )

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
#Vai adicionar a tarefa na tela
#(o parâmetro "carregando" vai indicar se as informações vem das informaçôes de dentro do banco de dados ou do criador de tarefas, pro programa entender oq ele está fazendo)    
def adicionar_tarefa(
    frame_dia,
    tela_principal,
    nome_da_tarefa,
    desc_da_tarefa,
    temp_ou_fix,
    hora_inicio=11,
    min_inicio=59,
    hora_fim=23,
    min_fim=59,
    dia_semana = '',
    check_state = 2,
    carregando = False,
    aba_atual = False
):
 
    try:
        
      #Título e criação do frame que vai acomodar as infs
        tarefa_criada = ctk.CTkFrame(
            frame_dia, 620, 200, border_color="purple2", border_width=1
        )
        tarefa_criada.pack(pady=7)
        
        if nome_da_tarefa == '':
            nome_da_tarefa = 'tarefa_sem_nome'
            
        
        title = ctk.CTkEntry(
            tarefa_criada,
            placeholder_text=nome_da_tarefa,
            placeholder_text_color='dodgerblue',
            width=500,
            font=("", 20),
        )
        title.place(x=10, y=10)
        title.configure(state="disabled")
        title.configure(placeholder_text="ovo")

         #Descrição
        desc = ctk.CTkTextbox(
            tarefa_criada, text_color='dodgerblue', width=500, height=100
        )
        desc.insert("0.0", desc_da_tarefa)
        desc.place(x=10, y=45)
        desc.configure(state="disabled")

        # Botão de editar
        def editar_taf(tela_principal,
                       dia_semana):
            tela_principal.geometry("1250x650")

            tarefatela = ctk.CTkFrame(
                tela_principal, 245, 635, border_color='yellow', border_width=1,fg_color='gray4')
            tarefatela.place(x=1000, y=10)

            nome_novo_da_tarefa = ctk.CTkEntry(
                tarefatela, 225, 25, placeholder_text="Título da Tarefa...",fg_color='gray9',border_color='gray4')
            nome_novo_da_tarefa.place(x=10, y=7)

            desc_nova_da_tarefa = ctk.CTkTextbox(tarefatela, 225, 200,fg_color='gray9')
            desc_nova_da_tarefa.place(x=10, y=39)
            desc_nova_da_tarefa.insert(index="0.0", text="Descrição da Tarefa...")
            
            def update_linha():
                print(aba_atual)
                if aba_atual == True:
                    geometria = '1000x650'
                else:
                    geometria = '1080x650'    
                
                tela_principal.geometry(geometria)    
                    
                id_linha = db.descobrir_id(nome_da_tarefa,desc_da_tarefa,dia_semana)
                
                if nome_novo_da_tarefa.get() == '':
                    nome_novo = 'tarefa_sem_nome'
                else:
                    nome_novo = nome_novo_da_tarefa.get()
                    
                db.editar_linha(id_linha,nome_novo,desc_nova_da_tarefa.get("1.0","end"))

                return (
                    title.configure(state="normal"),
                    title.configure(placeholder_text=nome_novo_da_tarefa.get()),
                    title.configure(state="disabled"),
                    desc.configure(state="normal"),
                    desc.delete("1.0", "end"),
                    desc.insert(index="0.0", text=desc_nova_da_tarefa.get("1.0", "end")),
                    desc.configure(state="disabled"),
                    excluir_btn.configure(state= 'disabled'),
                    edit_btn.configure(state='disabled'),
                    check.configure(state='disabled'),
                    tarefatela.destroy()
                )

            salvar_btn = ctk.CTkButton(
                tarefatela,
                text="EDITAR",
                fg_color='yellow',
                hover_color='gold3',
                text_color='black',
                width=225,
                height=25,
                command=update_linha,
            )
            salvar_btn.place(x=10, y=600)

        edit_btn = ctk.CTkButton(
            tarefa_criada,
            text="EDITAR",
            width=50,
            height=50,
            command=lambda: editar_taf(tela_principal,dia_semana),
        )
        edit_btn.place(x=525, y=55)

        # Fixo ou temporario
        if temp_ou_fix == 1:
            tarefa_criada.configure(border_color="yellow")
        elif temp_ou_fix == 2:
            tarefa_criada.configure(border_color='dodgerblue')
        else:
            temp_ou_fix = 3

        # Check Box
        estado_checkbox = ctk.IntVar(value=check_state)
        
        def decidir_dia_atual():
            day = datetime.datetime.now().strftime("%A")
            return day
        
        def chechagem():
            id_linha = db.descobrir_id(nome_da_tarefa,desc_da_tarefa,dia_semana)
            
            if estado_checkbox.get() == 1:
                db.cursor.execute('''UPDATE trax SET pontos = pontos + 1
                                      WHERE id = ?''',(id_linha,))
                
                db.cursor.execute('''UPDATE trax SET pontos = pontos + 1
                                      WHERE temporario = 1 AND id = ?''',(id_linha,))
                
                db.cursor.execute('''UPDATE trax SET checkbox = 1
                                  WHERE id = ?''', (id_linha,))
                
            if estado_checkbox.get() == 2:
                db.cursor.execute('''UPDATE trax SET pontos = pontos - 1
                                  WHERE id = ?''', (id_linha,))

                db.cursor.execute('''UPDATE trax SET pontos = pontos - 1
                                      WHERE temporario = 1 AND id = ?''',(id_linha,))
                
                db.cursor.execute('''UPDATE trax SET checkbox = 2
                                  WHERE id = ?''', (id_linha,))
                     
            db.conexao.commit()
          
        check = ctk.CTkCheckBox(
            tarefa_criada,
            text="",
            width=35,
            checkbox_width=35,
            checkbox_height=35,
            fg_color='dodgerblue',
            checkmark_color="green2",
            variable=estado_checkbox,
            onvalue=1,
            offvalue=2,
            command= chechagem
        )
        check.place(x=555, y=10)
           
        dia_atual = decidir_dia_atual()
        
        if dia_atual != dia_semana:
            check.configure(state = 'disabled')

        # Botão de excluir
        def excluir_taf():
            tarefa_criada.destroy()
            id_linha = db.descobrir_id(nome_da_tarefa,desc_da_tarefa,dia_semana)
            db.excluir_linha(id_linha)
        
        excluir_btn = ctk.CTkButton(
            tarefa_criada, text="EXCLUIR", width=50, height=50, command=excluir_taf
        )
        excluir_btn.place(x=525, y=110)

        # Tratamento de horário para salvar no banco de dados sem erros e no formato correto para funcionar na função notificadora
        if carregando == True:
            horainicio_text = ctk.CTkEntry(
            tarefa_criada,
            53,
            30,
            placeholder_text=hora_inicio,
            placeholder_text_color="green",
            )
            horainicio_text.place(x=190, y=155)
            horainicio_text.configure(state="disabled")

            horafim_text = ctk.CTkEntry(
                tarefa_criada,
                53,
                30,
                placeholder_text=hora_fim,
                placeholder_text_color="firebrick2",
            )
            horafim_text.place(x=270, y=155)
            horafim_text.configure(state="disabled")
        else:
            try:
                hora_inicio = int(hora_inicio)
            except:
                hora_inicio = 11
            
            try:       
                hora_fim = int(hora_fim)
            except:
                hora_fim = 23
            
            try:    
                min_inicio = int(min_inicio)
            except:
               min_inicio = 59
            
            try:
                min_fim = int(min_fim)
            except:
                min_fim = 59
            

            if hora_inicio > 23:
                hora_inicio = 11
            if min_inicio > 59:
                min_inicio = 59
            if hora_fim > 23:
                hora_fim = 23
            if min_fim > 59:
                min_fim = 59

            hora_inicio = str(hora_inicio).zfill(2)
            min_inicio = str(min_inicio).zfill(2)
            hora_fim = str(hora_fim).zfill(2)
            min_fim = str(min_fim).zfill(2)
            
            if len(hora_inicio) > 2 or len(hora_inicio) < 2:
                hora_inicio = 11
            if len(min_inicio) > 2 or len(min_inicio) < 2:
                min_inicio = 59
            if len(hora_fim) > 2 or len(hora_fim) < 2:
                hora_fim = 23
            if len(min_fim) > 2 or len(min_fim) < 2:
                min_fim = 59

            
            horainicio_text = ctk.CTkEntry(
                tarefa_criada,
                53,
                30,
                placeholder_text=f"{hora_inicio} : {min_inicio}",
                placeholder_text_color="green",
            )
            horainicio_text.place(x=190, y=155)
            horainicio_text.configure(state="disabled")

            horafim_text = ctk.CTkEntry(
                tarefa_criada,
                53,
                30,
                placeholder_text=f"{hora_fim} : {min_fim}",
                placeholder_text_color="firebrick2",
            )
            horafim_text.place(x=270, y=155)
            horafim_text.configure(state="disabled")

#Salva as informações no banco de dados caso não esteja apenas carregando as informações existentes
        if aba_atual == True:
            tela_principal.geometry("1000x650")
        else:
            tela_principal.geometry("1080x650")    
        if carregando == False:
            db.adicionar_linha(nome_da_tarefa,desc_da_tarefa,dia_semana,f'{hora_inicio}:{min_inicio}',f'{hora_fim}:{min_fim}',temp_ou_fix)
    except Exception as e:
        tela_principal.geometry("1000x650")
        print(e)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Uma aba dedicada para as tarefas do dia atual, a rotina diária
def rotina_atual(janela, tela_principal):
    for widget in janela.winfo_children():
        widget.destroy()

    tela_principal.geometry("1000x650")
    
    def decidir_dia_atual():
        day = datetime.datetime.now().strftime("%A")
        return day
    
    schedule.every(10).seconds.do(decidir_dia_atual)
    
    def loop_diario():
        schedule.run_pending()
        tela_principal.after(1000, loop_diario)
      
    
    dia_atual = decidir_dia_atual()
    
    
    dias(janela, tela_principal, dia_atual,True)
    
    #Vai desmarcar todas as checkboxs do dia atual e salvar os pontos, possibilitando uma "gamificação" das tarefas
    def encerrar_dia():
   
        dados = db.carregar_rotina(dia_atual)
            
        for linha in dados:
                db.cursor.execute('''UPDATE trax SET checkbox = 2 WHERE dia = ?''', (dia_atual,))
                db.conexao.commit()

        rotina_atual(janela,tela_principal)
            
            
    encerrar_dia_btn = ctk.CTkButton(
        janela,
        text="Encerrar Dia",
        fg_color= 'firebrick',
        hover_color='firebrick4',
        width=20,
        height=110,
        command= encerrar_dia
                )
    encerrar_dia_btn.place(x=742,y=255)
    
    loop_diario()
    tela_principal.geometry("1000x650")
    
#Vai mostrar a rotina que o usuário escolher, tem acesso a todos os dias da semana, para o usuário poder organizar sua rotina semanal ou apenas visualizar    
def rotinas(janela, tela_principal):
    
    def apagar():
        for widget in janela.winfo_children():
            widget.destroy()

    apagar()
    
    tela_principal.geometry("1080x650")
    
    segunda_btn = ctk.CTkButton(tela_principal,70,70,text='S',command=lambda:dias(janela,tela_principal,'Monday'))
    segunda_btn.place(x=1000,y=10)
        
    terça_btn = ctk.CTkButton(tela_principal,70,70,text='T',command=lambda:dias(janela,tela_principal,'Tuesday'))
    terça_btn.place(x=1000,y=90)
        
    quarta_btn = ctk.CTkButton(tela_principal,70,70,text='Q',command=lambda:dias(janela,tela_principal,'Wednesday'))
    quarta_btn.place(x=1000,y=170)    
        
    quinta_btn = ctk.CTkButton(tela_principal,70,70,text='Q',command=lambda:dias(janela,tela_principal,'Thursday'))
    quinta_btn.place(x=1000,y=250)
        
    sexta_btn = ctk.CTkButton(tela_principal,70,70,text='S',command=lambda:dias(janela,tela_principal,'Friday'))
    sexta_btn.place(x=1000,y=330)
        
    sabado_btn = ctk.CTkButton(tela_principal,70,70,text='S',command=lambda:dias(janela,tela_principal,'Saturday'))
    sabado_btn.place(x=1000,y=410)
        
    domingo_btn = ctk.CTkButton(tela_principal,70,70,text='D',command=lambda:dias(janela,tela_principal,'Sunday'))
    domingo_btn.place(x=1000,y=490)
    
    delete_tudo_btn = ctk.CTkButton(tela_principal,70,70,text='Delete',command=lambda:apagar())
    delete_tudo_btn.place(x=1000,y=570)
              