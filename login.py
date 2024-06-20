import customtkinter as ctk

# Configurações de aparência e tema

ctk.set_appearance_mode('blue')
ctk.set_default_color_theme('dark-blue')

# Criação da janela principal

janela = ctk.CTk()
janela.geometry("500x500")
janela.title("Janela Login")

def clique():
    print("Fazer login")

# Adicionar alguns widgets para observar as mudanças

texto = ctk.CTkLabel(janela, text="Login")
email = ctk.CTkEntry(janela, placeholder_text="E-mail")
senha = ctk.CTkEntry(janela, placeholder_text="Senha",show="*")

botao = ctk.CTkButton(janela, text="Login",command=clique, fg_color="red", hover_color="blue")

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

# Loop principal da janela

janela.mainloop()
