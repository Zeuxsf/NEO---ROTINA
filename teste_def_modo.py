import customtkinter

customtkinter.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x200")

def change_appearance_mode_event():
    new_mode = mode_optionemenu.get()
    customtkinter.set_appearance_mode(new_mode)

mode_label = customtkinter.CTkLabel(app, text="Appearance Mode:")
mode_label.pack(padx=20, pady=10)

mode_optionemenu = customtkinter.CTkOptionMenu(app, values=["Light", "Dark", "System"],
                                                command=change_appearance_mode_event)
mode_optionemenu.pack(padx=20, pady=10)
mode_optionemenu.set("System")

app.mainloop()