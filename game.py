import tkinter as tk
from tkinter import messagebox

NUMERO_SECRETO = 7

def verificar_palpite():
    try:
        palpite = int(entry_palpite.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")
        return

    if palpite == NUMERO_SECRETO:
        messagebox.showinfo("Resultado", "🎉 Parabéns! Você acertou o número secreto!")
    else:
        messagebox.showwarning("Resultado", "❌ Errou! Tente novamente!")

def jogar_novamente():
    entry_palpite.delete(0, tk.END)

janela = tk.Tk()
janela.title("Jogo: Adivinhe o Número")
janela.geometry("350x250")

label_titulo = tk.Label(janela, text="Adivinhe o número secreto (0 a 10)", font=("Arial", 12))
label_titulo.pack(pady=10)

entry_palpite = tk.Entry(janela, font=("Arial", 12), justify="center")
entry_palpite.pack(pady=5)

btn_verificar = tk.Button(janela, text="Verificar", font=("Arial", 12), command=verificar_palpite)
btn_verificar.pack(pady=10)

btn_reiniciar = tk.Button(janela, text="Jogar Novamente", font=("Arial", 12), command=jogar_novamente)
btn_reiniciar.pack(pady=5)

janela.mainloop()
