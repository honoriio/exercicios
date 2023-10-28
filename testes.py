import tkinter as tk

# Função a ser chamada quando o botão for pressionado
def greet():
    print("Hello, Tkinter!")

# Cria a janela principal
root = tk.Tk()

# Adiciona um rótulo à janela
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(padx=20, pady=20)  # Adiciona espaçamento ao redor do widget

# Adiciona um botão à janela
button = tk.Button(root, text="Greet", command=greet)
button.pack(padx=20, pady=20)  # Adiciona espaçamento ao redor do widget

# Inicia o loop principal
root.mainloop()
