import customtkinter as ctk
import tkinter as tk
from pystray import Icon, MenuItem as item, Menu
from PIL import Image
import threading

# Funções do Tray
def esconder_janela():
    root.withdraw()
    mostrar_tray()

def mostrar_janela(icon=None, item=None):
    root.deiconify()
    tray.stop()

def sair_do_programa(icon, item):
    tray.stop()
    root.destroy()

def mostrar_tray():
    global tray
    image = Image.open("imagens/ntx_logo.ico")  # Ícone 16x16 ou 32x32
    menu = Menu(
        item('Abrir NeoTrax', mostrar_janela),
        item('Sair', sair_do_programa)
    )
    tray = Icon("NeoTrax", image, "Sua nova trilha!", menu)
    threading.Thread(target=tray.run).start()

# Janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # Ou o teu tema customizado
root = ctk.CTk()
root.geometry("400x300")
root.title("NeoTrax")

# Botão de minimizar pra bandeja
botao = ctk.CTkButton(root, text="Minimizar pra bandeja", command=esconder_janela)
botao.pack(pady=20)

# ... [restante do seu código] ...

# Detectar minimizar para esconder a janela
def checar_minimizacao():
    if root.state() == 'iconic':
        esconder_janela()
    root.after(1000, checar_minimizacao)

# Iniciar checagem de minimizar
checar_minimizacao()

root.mainloop()