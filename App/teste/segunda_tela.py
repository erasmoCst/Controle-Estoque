import tkinter as tk

class SegundaTela(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Segunda Tela")
        self.parent = parent

        self.label_numero1 = tk.Label(self, text="Número 1:")
        self.label_numero1.pack()
        self.entrada_numero1 = tk.Entry(self)
        self.entrada_numero1.pack()

        self.label_numero2 = tk.Label(self, text="Número 2:")
        self.label_numero2.pack()
        self.entrada_numero2 = tk.Entry(self)
        self.entrada_numero2.pack()

        self.botao_calcular = tk.Button(self, text="Calcular Soma", command=self.calcular_soma)
        self.botao_calcular.pack()

    def calcular_soma(self):
        try:
            numero1 = int(self.entrada_numero1.get())
            numero2 = int(self.entrada_numero2.get())
            resultado = numero1 + numero2
            # Chama o método na tela principal para atualizar o resultado lá
            self.parent.atualizar_resultado(resultado)
            self.destroy()
        except ValueError:
            # Mostra uma mensagem de erro caso os números não sejam válidos
            tk.messagebox.showerror("Erro", "Por favor, insira números válidos!")
