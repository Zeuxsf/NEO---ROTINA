import customtkinter as ctk
import salvar_carregar as j

carregar = j.carregar_rotina("arquivo_rotina.json")

# Área de cores:
dark_ou_light = "dark"
ctk.set_appearance_mode(dark_ou_light)
if dark_ou_light == "dark":
    cor_principal = "dodgerblue"
else:
    cor_principal = "red"


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

    hora_inicio = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="00")
    min_inicio = ctk.CTkEntry(tarefatela, 35, 10, placeholder_text="00")
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
        command=lambda: salvar_configs_tarefa(
            frame_dia,
            tarefatela,
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



# Sistema de frames para cada dia da semana, para auxiliar na organização
def dias(tela, tela_principal, mostrar=False):

    def segunda():
        if "seg" in mostrar:
            segunda_frame = ctk.CTkScrollableFrame(tela, 820, 651)
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

    def terça():
        if "ter" in mostrar:
            terça_frame = ctk.CTkScrollableFrame(tela, 820, 651)
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

    def quarta():
        if "qua" in mostrar:
            quarta_frame = ctk.CTkScrollableFrame(tela, 820, 651)
            quarta_frame.pack(pady=5)

    def quinta():
        if "qui" in mostrar:
            quinta_frame = ctk.CTkScrollableFrame(tela, 820, 651)
            quinta_frame.pack(pady=5)

    def sexta():
        if "sex" in mostrar:
            sexta_frame = ctk.CTkScrollableFrame(tela, 820, 651)
            sexta_frame.pack(pady=5)

    def sabado():
        if "sab" in mostrar:
            sabado_frame = ctk.CTkScrollableFrame(tela, 820, 651)
            sabado_frame.pack(pady=5)

    def domingo():
        if "dom" in mostrar:
            domingo_frame = ctk.CTkScrollableFrame(tela, 820, 651)
            domingo_frame.pack(pady=5)

    segunda()
    terça()
    quarta()
    quinta()
    sexta()
    sabado()
    domingo()


def rotina_atual(jnl, tela_principal):
    for widget in jnl.winfo_children():
        widget.destroy()

    tela_principal.geometry("1000x650")
    dias(jnl, tela_principal, "seg")


def rotinas(jnl, tela_principal):
    for widget in jnl.winfo_children():
        widget.destroy()
    tela_principal.geometry("1000x650")
    dias(jnl, tela_principal, "seg,ter,qua,qui,sex,sab,dom")



def salvar_configs_tarefa(
    frame_dia,
    tarefatela,
    tela_principal,
    nome_taf,
    desc_taf,
    temp_ou_fix,
    horainicio=11,
    mininicio=59,
    horafim=23,
    minfim=59,
    dia_semana = None
):


    try:
#------------------------------------------------------------------------------------------------------------------------
      #Título e criação do frame que vai acomodar as infs
        tarefa_salva = ctk.CTkFrame(
            frame_dia, 620, 200, border_color="purple2", border_width=1
        )
        tarefa_salva.pack(pady=7)

        title = ctk.CTkEntry(
            tarefa_salva,
            placeholder_text=nome_taf,
            placeholder_text_color=cor_principal,
            width=500,
            font=("", 20),
        )
        title.place(x=10, y=10)
        title.configure(state="disabled")
        title.configure(placeholder_text="ovo")
#------------------------------------------------------------------------------------------------------------------------
         #Descrição
        desc = ctk.CTkTextbox(
            tarefa_salva, text_color=cor_principal, width=500, height=100
        )
        desc.insert("0.0", desc_taf)
        desc.place(x=10, y=45)
        desc.configure(state="disabled")
#------------------------------------------------------------------------------------------------------------------------
        # Botão de editar
        def editar_taf(tela_principal, nome_antigo, ide):
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

                dados = j.carregar_rotina("arquivo_rotina.json")

                del dados[nome_antigo]

                dados[nome_da_tarefa.get()] = {
                    "desc": desc_da_tarefa.get("1.0", "end"),
                    "id": ide,
                }

                j.salvar_rotina("arquivo_rotina.json", dados)

                return (
                    title.configure(state="normal"),
                    title.configure(placeholder_text=nome_da_tarefa.get()),
                    title.configure(state="disabled"),
                    desc.configure(state="normal"),
                    desc.delete("1.0", "end"),
                    desc.insert(index="0.0", text=desc_da_tarefa.get("1.0", "end")),
                    desc.configure(state="disabled"),
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
            tarefa_salva,
            text="EDITAR",
            width=50,
            height=50,
            command=lambda: editar_taf(tela_principal, nome_taf),
        )
        edit_btn.place(x=525, y=55)
#------------------------------------------------------------------------------------------------------------------------
        # Fixo ou temporario
        if temp_ou_fix == 1:
            tarefa_salva.configure(border_color="yellow")
        elif temp_ou_fix == 2:
            tarefa_salva.configure(border_color=cor_principal)
        else:
            temp_ou_fix = 3
#------------------------------------------------------------------------------------------------------------------------
        # Check Box
        check = ctk.CTkCheckBox(
            tarefa_salva,
            text="",
            width=35,
            checkbox_width=35,
            checkbox_height=35,
            fg_color=cor_principal,
            checkmark_color="green2",
        )
        check.place(x=555, y=10)
#------------------------------------------------------------------------------------------------------------------------
        # Botão de excluir
        def excluir_taf():
            tarefa_salva.destroy()
            dados = j.carregar_rotina("arquivo_rotina.json")

            del dados[nome_taf]

            j.salvar_rotina("arquivo_rotina.json", dados)

        excluir_btn = ctk.CTkButton(
            tarefa_salva, text="EXCLUIR", width=50, height=50, command=excluir_taf
        )
        excluir_btn.place(x=525, y=110)
#------------------------------------------------------------------------------------------------------------------------
        # Horario
        if len(horainicio) > 2 or len(horainicio) < 2:
            horainicio = None
        if len(mininicio) > 2 or len(mininicio) < 2:
            mininicio = None
        if len(horafim) > 2 or len(horafim) < 2:
            horafim = None
        if len(minfim) > 2 or len(minfim) < 2:
            minfim = None

        try:
            horainicio = int(horainicio)
        except:
           horainicio = 11
        
        try:       
            horafim = int(horafim)
        except:
           horafim = 23
        
        try:    
            mininicio = int(mininicio)
        except:
           mininicio = 59
        
        try:
           minfim = int(minfim)
        except:
           minfim = 59
          

        if horainicio > 23:
            horainicio = 11
        if mininicio > 59:
            mininicio = 59
        if horafim > 23:
            horafim = 23
        if minfim > 59:
            minfim = 59

        horainicio_text = ctk.CTkEntry(
            tarefa_salva,
            53,
            30,
            placeholder_text=f"{horainicio} : {mininicio}",
            placeholder_text_color="green",
        )
        horainicio_text.place(x=190, y=155)
        horainicio_text.configure(state="disabled")

        horafim_text = ctk.CTkEntry(
            tarefa_salva,
            53,
            30,
            placeholder_text=f"{horafim} : {minfim}",
            placeholder_text_color="firebrick2",
        )
        horafim_text.place(x=270, y=155)
        horafim_text.configure(state="disabled")
#------------------------------------------------------------------------------------------------------------------------
#FIM
        tarefatela.destroy()
        tela_principal.geometry("1000x650")
        

        dados = j.carregar_rotina("arquivo_rotina.json")

        dados[nome_taf] = {
            "desc": desc_taf,
            "horaini": f"{horainicio}:{mininicio}",
            "horafim": f"{horafim}:{minfim}",
            "dia": dia_semana,
            "tempo": temp_ou_fix
            }

        j.salvar_rotina("arquivo_rotina.json", dados)
        
    except:
        tarefatela.destroy()
        tela_principal.geometry("1000x650")
