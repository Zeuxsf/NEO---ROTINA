import customtkinter as ctk
import salvar_carregar as j

# Área de cores:
dark_ou_light = "dark"
ctk.set_appearance_mode(dark_ou_light)
if dark_ou_light == "dark":
    cor_principal = "dodgerblue"
else:
    cor_principal = "red"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def criador_de_tarefas(frame_dia, tela_principal,dia):

    tela_principal.geometry("1250x650")

    tarefatela = ctk.CTkFrame(
        tela_principal, 245, 635, border_color=cor_principal, border_width=1
    )
    tarefatela.place(x=1000, y=10)

    nome_da_tarefa = ctk.CTkEntry(
        tarefatela, 225, 25, placeholder_text="Título da Tarefa..."
    )
    nome_da_tarefa.place(x=10, y=7)

    desc_da_tarefa = ctk.CTkTextbox(tarefatela, 225, 200)
    desc_da_tarefa.place(x=10, y=39)
    desc_da_tarefa.insert(index="0.0", text="Descrição da Tarefa...")

    hora_texto = ctk.CTkLabel(
        tarefatela, text="Hora de ínicio.        Hora de encerramento."
    )
    hora_texto.place(x=7, y=239)

    hora_inicio = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="11")
    min_inicio = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="59")
    hora_inicio.place(x=7, y=265)
    min_inicio.place(x=47, y=265)

    hora_fim = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="23")
    min_fim = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="59")
    hora_fim.place(x=140, y=265)
    min_fim.place(x=180, y=265)

    variavel_escolha = ctk.IntVar(value=0)

    temporario_escolha = ctk.CTkRadioButton(
        tarefatela, text="Temporária", variable=variavel_escolha, value=1
    )
    fixo_escolha = ctk.CTkRadioButton(
        tarefatela, text="Fixa", variable=variavel_escolha, value=2
    )
    temporario_escolha.place(x=15, y=310)
    fixo_escolha.place(x=130, y=310)

    salvar_btn = ctk.CTkButton(
        tarefatela,
        text="SALVAR",
        fg_color=cor_principal,
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
            dia
        ),
    )
    salvar_btn.place(x=10, y=600)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Carregador de tarefas
def iniciar_tela_rotina(frame_dia,tela_principal,dia):
    dados = j.carregar_rotina(dia)
    
    for nome_tarefa, info in dados.items():
        if info['dia'] == dia:
            adicionar_tarefa(frame_dia=frame_dia,
                         nome_da_tarefa=nome_tarefa,
                         desc_da_tarefa=info['desc'],
                         temp_ou_fix=info['tempo'],
                         hora_inicio=info['hora_inicio'],
                         hora_fim=info['hora_fim'],
                         dia_semana=info['dia'],
                         check_state = info['checkbox'],
                         tela_principal=tela_principal
                         )
        
        


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sistema de frames para cada dia da semana, para auxiliar na organização
def dias(janela, tela_principal, mostrar=False):

    def segunda():
        if "seg" in mostrar:
            segunda_frame = ctk.CTkScrollableFrame(janela, 820, 651)
            segunda_frame.pack(pady=5)

            title = ctk.CTkLabel(segunda_frame, text="Segunda", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton(
                segunda_frame,
                text="+",
                fg_color=cor_principal,
                width=20,
                height=20,
                command=lambda: criador_de_tarefas(segunda_frame, tela_principal,'seg'),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(segunda_frame,tela_principal,'seg')

    def terça():
        if "ter" in mostrar:
            terça_frame = ctk.CTkScrollableFrame(janela, 820, 651)
            terça_frame.pack(pady=5)

            title = ctk.CTkLabel(terça_frame, text="Terça", font=("", 35))
            title.pack(pady=15)

            add_tarefa_btn = ctk.CTkButton(
                terça_frame,
                text="+",
                fg_color=cor_principal,
                width=20,
                height=20,
                command=lambda: criador_de_tarefas(terça_frame, tela_principal,'ter'),
            )
            add_tarefa_btn.place(x=490, y=30)
            
            iniciar_tela_rotina(terça_frame,tela_principal,'ter')

    def quarta():
        if "qua" in mostrar:
            quarta_frame = ctk.CTkScrollableFrame(janela, 820, 651)
            quarta_frame.pack(pady=5)

    def quinta():
        if "qui" in mostrar:
            quinta_frame = ctk.CTkScrollableFrame(janela, 820, 651)
            quinta_frame.pack(pady=5)

    def sexta():
        if "sex" in mostrar:
            sexta_frame = ctk.CTkScrollableFrame(janela, 820, 651)
            sexta_frame.pack(pady=5)

    def sabado():
        if "sab" in mostrar:
            sabado_frame = ctk.CTkScrollableFrame(janela, 820, 651)
            sabado_frame.pack(pady=5)

    def domingo():
        if "dom" in mostrar:
            domingo_frame = ctk.CTkScrollableFrame(janela, 820, 651)
            domingo_frame.pack(pady=5)

    segunda()
    terça()
    quarta()
    quinta()
    sexta()
    sabado()
    domingo()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    check_state = 0
):


    try:
      #Título e criação do frame que vai acomodar as infs
        tarefa_criada = ctk.CTkFrame(
            frame_dia, 620, 200, border_color="purple2", border_width=1
        )
        tarefa_criada.pack(pady=7)
        
        dados = j.carregar_rotina('arquivo_rotina.json')
        
        if nome_da_tarefa == '':
            nome_da_tarefa = 'tarefa_sem_nome'
            
        
        title = ctk.CTkEntry(
            tarefa_criada,
            placeholder_text=nome_da_tarefa,
            placeholder_text_color=cor_principal,
            width=500,
            font=("", 20),
        )
        title.place(x=10, y=10)
        title.configure(state="disabled")
        title.configure(placeholder_text="ovo")

         #Descrição
        desc = ctk.CTkTextbox(
            tarefa_criada, text_color=cor_principal, width=500, height=100
        )
        desc.insert("0.0", desc_da_tarefa)
        desc.place(x=10, y=45)
        desc.configure(state="disabled")

        # Botão de editar
        def editar_taf(tela_principal,
                       nome_antigo,
                       hora_inicio,min_inicio,
                       hora_fim,min_fim,
                       dia_semana,
                       temp_ou_fix):
            tela_principal.geometry("1250x650")

            tarefatela = ctk.CTkFrame(
                tela_principal, 245, 635, border_color=cor_principal, border_width=1
            )
            tarefatela.place(x=1000, y=10)

            nome_da_tarefa = ctk.CTkEntry(
                tarefatela, 225, 25, placeholder_text="Título da Tarefa..."
            )
            nome_da_tarefa.place(x=10, y=7)

            desc_da_tarefa = ctk.CTkTextbox(tarefatela, 225, 200)
            desc_da_tarefa.place(x=10, y=39)
            desc_da_tarefa.insert(index="0.0", text="Descrição da Tarefa...")

            def editar_tarefa():
                nonlocal nome_antigo

                tela_principal.geometry("1000x650")

                dados = j.carregar_rotina(dia_semana)

                del dados[nome_antigo]

                dados[nome_da_tarefa.get()] = {
                    "desc": desc_da_tarefa.get('1.0','end'),
                    "hora_inicio": f"{hora_inicio}:{min_inicio}",
                    "hora_fim": f"{hora_fim}:{min_fim}",
                    "dia": dia_semana,
                    "tempo": temp_ou_fix,
                    "checkbox": estado_checkbox.get()
                    
                }

                j.salvar_rotina(dia_semana, dados)

                return (
                    title.configure(state="normal"),
                    title.configure(placeholder_text=nome_da_tarefa.get()),
                    title.configure(state="disabled"),
                    desc.configure(state="normal"),
                    desc.delete("1.0", "end"),
                    desc.insert(index="0.0", text=desc_da_tarefa.get("1.0", "end")),
                    desc.configure(state="disabled"),
                    excluir_btn.configure(state= 'disabled'),
                    edit_btn.configure(state='disabled'),
                    check.configure(state='disabled')
                )

            salvar_btn = ctk.CTkButton(
                tarefatela,
                text="EDITAR",
                fg_color=cor_principal,
                width=225,
                height=25,
                command=editar_tarefa,
            )
            salvar_btn.place(x=10, y=600)

        edit_btn = ctk.CTkButton(
            tarefa_criada,
            text="EDITAR",
            width=50,
            height=50,
            command=lambda: editar_taf(tela_principal, nome_da_tarefa,hora_inicio,min_inicio,hora_fim,min_fim,dia_semana,temp_ou_fix),
        )
        edit_btn.place(x=525, y=55)

        # Fixo ou temporario
        if temp_ou_fix == 1:
            tarefa_criada.configure(border_color="yellow")
        elif temp_ou_fix == 2:
            tarefa_criada.configure(border_color=cor_principal)
        else:
            temp_ou_fix = 3

        # Check Box
        estado_checkbox = ctk.IntVar(value=check_state)
        
        def chechagem():
            dados = j.carregar_rotina(dia_semana)
            
            dados[nome_da_tarefa]['checkbox'] = estado_checkbox.get()
            
            j.salvar_rotina(dia_semana,dados)   
          
        check = ctk.CTkCheckBox(
            tarefa_criada,
            text="",
            width=35,
            checkbox_width=35,
            checkbox_height=35,
            fg_color=cor_principal,
            checkmark_color="green2",
            variable=estado_checkbox,
            onvalue=1,
            offvalue=2,
            command= chechagem
        )
        check.place(x=555, y=10)

        # Botão de excluir
        def excluir_taf():
            tarefa_criada.destroy()
            dados = j.carregar_rotina(dia_semana)

            del dados[nome_da_tarefa]

            j.salvar_rotina(dia_semana, dados)
        
        excluir_btn = ctk.CTkButton(
            tarefa_criada, text="EXCLUIR", width=50, height=50, command=excluir_taf
        )
        excluir_btn.place(x=525, y=110)

        # Horario
        if len(hora_inicio) > 2 or len(hora_inicio) < 2:
            hora_inicio = 11
        if len(min_inicio) > 2 or len(min_inicio) < 2:
            min_inicio = 59
        if len(hora_fim) > 2 or len(hora_fim) < 2:
            hora_fim = 23
        if len(min_fim) > 2 or len(min_fim) < 2:
            min_fim = 59

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

#FIM
        tela_principal.geometry("1000x650")
        

        dados = j.carregar_rotina(dia_semana)
        
        dados[nome_da_tarefa] = {
            "desc": desc_da_tarefa,
            "hora_inicio": f"{hora_inicio}:{min_inicio}",
            "hora_fim": f"{hora_fim}:{min_fim}",
            "dia": dia_semana,
            "tempo": temp_ou_fix,
            "checkbox": estado_checkbox.get(),
            }

        j.salvar_rotina(dia_semana, dados)
        
    except:
        tela_principal.geometry("1000x650")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def rotina_atual(janela, tela_principal):
    for widget in janela.winfo_children():
        widget.destroy()

    tela_principal.geometry("1000x650")
    dias(janela, tela_principal, "seg")


def rotinas(janela, tela_principal):
    for widget in janela.winfo_children():
        widget.destroy()
    tela_principal.geometry("1000x650")
    dias(janela, tela_principal, "seg,ter,qua,qui,sex,sab,dom")
