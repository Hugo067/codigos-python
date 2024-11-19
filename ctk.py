#celso
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry('000x000')
ctk.set_appearance_mode('white')

texto= ctk.CTkLabel(janela, text=("ola mundo"))
texto.pack()
num = ctk.CTkEntry(janela,placeholder_text=("digite = "))
num.pack()
botao = ctk.CTkButton(janela,text=("comfirma"))
botao.pack()





janela.mainloop()