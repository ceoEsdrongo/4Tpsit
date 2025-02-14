import tkinter as tk
from tkinter.font import Font

class Finestra(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Anagrafica")
        self.master.geometry("600x400")
        self.grid()
        self.lista_dati = []  # Lista di dizionari per i dati
        self.crea_Widgets()

    def crea_Widgets(self):
        fontMod = Font(family='Calibri', size=12)

        # LABELS & ENTRY
        self.label_titolo = tk.Label(self, text="Dati Anagrafici", fg="red", font=("Helvetica", 20))
        self.label_titolo.grid(row=0, column=1, columnspan=3)

        campi = ["Nome", "Cognome", "Indirizzo", "C.F.", "Data Nascita", "Mail", "Tel."]
        self.valori = {}
        for i, campo in enumerate(campi):
            tk.Label(self, text=f"{campo}:", font=fontMod).grid(row=i+1, column=0, sticky='w')
            self.valori[campo] = tk.StringVar()
            tk.Entry(self, textvariable=self.valori[campo]).grid(row=i+1, column=1)

        # RADIOBUTTONS per il genere
        tk.Label(self, text="Genere:", font=fontMod).grid(row=5, column=2, sticky='w')
        self.vr = tk.StringVar(value="Nessuno")
        tk.Radiobutton(self, text='M', variable=self.vr, value='M').grid(row=5, column=3, sticky='w')
        tk.Radiobutton(self, text='F', variable=self.vr, value='F').grid(row=5, column=4, sticky='w')

        # TEXTAREA
        self.text_area = tk.Text(self, height=5, width=60)
        self.text_area.grid(row=9, column=0, columnspan=4, pady=10)

        # BOTTONI
        tk.Button(self, text="Salva", command=self.salva).grid(row=8, column=0)
        tk.Button(self, text="Pulisci", command=self.pulisci).grid(row=8, column=1)
        tk.Button(self, text="Stampa", command=self.stampa).grid(row=8, column=2)
        tk.Button(self, text="Esci", command=self.master.quit).grid(row=8, column=3)

    def salva(self):
        dati = {campo: self.valori[campo].get() for campo in self.valori}
        dati["Genere"] = self.vr.get()
        self.lista_dati.append(dati)

        with open("anagrafica.txt", "a") as file:
            file.write(str(dati) + "\n")

        self.text_area.insert(tk.END, str(dati) + "\n")

    def stampa(self):
        print("Dati salvati:")
        for dati in self.lista_dati:
            print(dati)

    def pulisci(self):
        for campo in self.valori:
            self.valori[campo].set("")
        self.vr.set("Nessuno")
        self.text_area.delete("1.0", tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = Finestra(master=root)
    app.mainloop()
