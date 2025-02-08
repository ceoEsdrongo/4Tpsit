import tkinter as tk
from tkinter.font import Font


class Finestra(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Anagrafica")
        self.master.geometry("550x350")
        self.grid()
        self.crea_Widgets()

    def crea_Widgets(self):
        fontMod = Font(family= 'Calibri', size= 14)

        # LABEL
        self.label = tk.Label(self, text="Nome: ", font= fontMod)
        self.label.grid(row= 0, column= 0)

        self.valoreStr = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreStr)
        self.entry.grid(row=0, column=1)

        self.label = tk.Label(self, text="Cognome: ", font= fontMod)
        self.label.grid(row=0, column=3)

        self.valoreStr = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreStr)
        self.entry.grid(row=0,column=4)

        self.label = tk.Label(self, text="Indirizzo: ", font= fontMod)
        self.label.grid(row=1, column=0)

        self.valoreStr = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreStr)
        self.entry.grid(row=1,column=1)

        self.label = tk.Label(self, text="C.F.: ", font= fontMod)
        self.label.grid(row=2, column=0)

        self.valoreStr = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreStr)
        self.entry.grid(row=2,column=1)

        self.label = tk.Label(self, text="Data Nascita: ", font= fontMod)
        self.label.grid(row=3, column=0)

        self.valoreStr = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreStr)
        self.entry.grid(row=3,column=1)

        self.label = tk.Label(self, text="Genere: ", font= fontMod)
        self.label.grid(row=4, column=0)
        # Radiobutton
        self.vr = tk.IntVar(value = 1)
        self.radio1 = tk.Radiobutton(self, text='M', variable= self.vr, value= 1, command= self.radio)
        self.radio1.grid(row= 4, column= 1, sticky= tk.W)
        self.radio2 = tk.Radiobutton(self, text='F', variable=self.vr, value=2, command= self.radio)
        self.radio2.grid(row=4, column=2, sticky= tk.W)

        self.label = tk.Label(self, text="Mail: ", font= fontMod)
        self.label.grid(row=5, column=0)

        self.valoreStr = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreStr)
        self.entry.grid(row=5, column=1)

        self.label = tk.Label(self, text="Tel.: ", font= fontMod)
        self.label.grid(row=6, column=0)

        self.valoreStr = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreStr)
        self.entry.grid(row=6, column=1)

        # BOTTONI
        self.button = tk.Button(self, text="Salva")
        self.button.grid(row=8, column=0)

        self.button = tk.Button(self, text="Cancella")
        self.button.grid(row=8, column=1)

        self.button = tk.Button(self, text="Stampa")
        self.button.grid(row=8, column=2)

        self.button = tk.Button(self, text="Chiudi")
        self.button.grid(row=8, column=3)

    def radio(self):
        print("Hai scelto: " , str(self.vr.get()))

if __name__ == '__main__':
    Finestra().mainloop()
