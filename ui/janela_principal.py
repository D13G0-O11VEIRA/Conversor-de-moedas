import tkinter as tk
from tkinter import ttk, messagebox

from services.api_cambio import (
    obter_moedas,
    converter
)


class JanelaPrincipal:

    def __init__(self):

        self.moedas = obter_moedas()

        self.janela = tk.Tk()
        self.janela.title("Conversor de Moedas")
        self.janela.geometry("500x350")
        self.janela.resizable(False, False)

        # Campo de valor
        self.entry_valor = tk.Entry(self.janela)
        self.entry_valor.pack(pady=10)

        # Combobox origem
        self.combo_origem = ttk.Combobox(
            self.janela,
            values=self.moedas,
            state="readonly"
        )
        self.combo_origem.pack(pady=5)

        # Combobox destino
        self.combo_destino = ttk.Combobox(
            self.janela,
            values=self.moedas,
            state="readonly"
        )
        self.combo_destino.pack(pady=5)

        # Valores padrão
        if "BRL" in self.moedas:
            self.combo_origem.set("BRL")

        if "USD" in self.moedas:
            self.combo_destino.set("USD")

        # Botão inverter
        self.btn_inverter = tk.Button(
            self.janela,
            text="↔ Inverter Moedas",
            command=self.clicar_inverter
        )
        self.btn_inverter.pack(pady=10)

        # Botão converter
        self.btn_converter = tk.Button(
            self.janela,
            text="Converter",
            command=self.clicar_converter
        )
        self.btn_converter.pack(pady=10)

        # Resultado
        self.resultado = tk.Label(
            self.janela,
            text="",
            font=("Arial", 11, "bold")
        )
        self.resultado.pack(pady=10)

    def clicar_converter(self):

        try:
            valor = float(
                self.entry_valor.get()
            )

            origem = self.combo_origem.get()
            destino = self.combo_destino.get()

            valor_convertido, taxa = converter(
                valor,
                origem,
                destino
            )

            self.resultado.config(
                text=(
                    f"{valor:.2f} {origem} = "
                    f"{valor_convertido:.2f} {destino}\n"
                    f"Taxa: 1 {origem} = {taxa:.4f} {destino}"
                )
            )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def clicar_inverter(self):

        origem = self.combo_origem.get()
        destino = self.combo_destino.get()

        self.combo_origem.set(destino)
        self.combo_destino.set(origem)

        if self.entry_valor.get():
            self.clicar_converter()


def iniciar():

    app = JanelaPrincipal()

    app.janela.mainloop()