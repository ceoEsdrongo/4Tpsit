import tkinter as tk


class Esempio(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Primo Esempio')
        self.master.geometry('300x300')
        self.grid()
        self.crea_widgets()

    def crea_widgets(self):
        self.etichetta1 = tk.Label(self, text='Inserisci il nome: ')
        self.etichetta1.grid(row=0, column=0)

        # stringa inserita dall'utente
        self.valoreStr = tk.StringVar()
        self.txtDato = tk.Entry(self, textvariable=self.valoreStr)
        self.txtDato.grid(row=0, column=1)

        self.pulsante = tk.Button(self, text='Scrivi', command=msg2)
        self.pulsante.grid(row=3, column=0)


        self.etichetta1 = tk.Label(self, text='Inserisci il cognome: ')
        self.etichetta1.grid(row=1, column=0)

        self.etichetta1 = tk.Label(self, text='Inserisci l\'indirzzo: ')
        self.etichetta1.grid(row=0, column=0)

        # stringa inserita dall'utente
        self.valoreStr = tk.StringVar()
        self.txtDato = tk.Entry(self, textvariable=self.valoreStr)
        self.txtDato.grid(row=0, column=1)

        self.pulsante = tk.Button(self, text='Scrivi', command=msg2)
        self.pulsante.grid(row=3, column=0)









        # stringa inserita dall'utente
        self.valoreStr = tk.StringVar()
        self.txtDato = tk.Entry(self, textvariable=self.valoreStr)
        self.txtDato.grid(row=1, column=1)

        self.pulsante = tk.Button(self, text='Scrivi', command=msg2)
        self.pulsante.grid(row=3, column=1)

        self.valoreStr = tk.StringVar()
        self.txtDato = tk.Entry(self, textvariable=self.valoreStr)
        self.txtDato.grid(row=1, column=1)

        self.pulsante = tk.Button(self, text='Scrivi', command=msg2)
        self.pulsante.grid(row=3, column=1)


def msg2(self):
    # Viene acquisito il valore della stringa utente
    valore = self.valoreStr.set()
    # Viene creata un'etichetta con il valore della stringa utente
    self.etichetta1 = tk.Label(self, text=valore)
    self.etichetta1.grid(row=2, column=0)


if __name__ == '__main__':
    Esempio().mainloop()

