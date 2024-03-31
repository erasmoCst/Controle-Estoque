import tkinter as tk
from segunda_tela import SegundaTela

class TelaInicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela Inicial")

        self.label_instrucao = tk.Label(self, text="Clique no botão para abrir a segunda tela e calcular a soma.")
        self.label_instrucao.pack(pady=20)

        self.botao_abrir = tk.Button(self, text="Abrir Segunda Tela", command=self.abrir_segunda_tela)
        self.botao_abrir.pack()

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack()

    def abrir_segunda_tela(self):
        segunda_tela = SegundaTela(self)
        segunda_tela.grab_set()  # Impede interação com a tela anterior enquanto a segunda está aberta

    def atualizar_resultado(self, resultado):
        self.label_resultado.config(text="O resultado da soma é: " + str(resultado))


if __name__ == "__main__":
    app = TelaInicial()
    app.mainloop()
