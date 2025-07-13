import os
import sys
import winreg

def iniciar_com_windows(indicador=True):
   
   if indicador == True:
    nome_app = "NeoTrax"
    caminho = os.path.abspath(sys.argv[0])

    chave = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )
    winreg.SetValueEx(chave, nome_app, 0, winreg.REG_SZ, caminho)
    winreg.CloseKey(chave)
   
   else: 
    nome_app = "NeoTrax"
    try:
        chave = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.DeleteValue(chave, nome_app)
        winreg.CloseKey(chave)
    except FileNotFoundError:
        pass    