'''
Allegro Elena
4AI

Partendo dallo script Grafica01, esempio a pag.308 del libro di testo
realizzare un'interfaccia grafica ANAGRAFICA.
Usare Label, Entry, Button, Radiobutton per interagire con l'utente e chiedere nome, cognome, indirizzo,
mail, telefono, CF, sesso, Data Nascita.
Creare quattro pulsanti: SALVA, PULISCI, STAMPA, ESCI per gestire i dati inseriti.

'''
import tkinter as tk
from tkinter.font import Font

from pyparsing import line_start


class Finestra(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Anagrafica")
        self.master.geometry("540x300")
        self.grid()
        self.crea_Widgets()
        self.lista= []

    def crea_Widgets(self):
        fontMod = Font(family= 'Calibri', size= 12)

        # LABEL
        self.label = tk.Label(self, text= "Dati Anagrafici", fg= "red", font= ("Helvetics", 20))
        self.label.grid(row=0 , column= 1)

        self.label = tk.Label(self, text="Nome: ", font= fontMod)
        self.label.grid(row= 1, column= 0)
        self.valoreNome = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreNome)
        self.entry.grid(row=1, column=1)

        self.label = tk.Label(self, text="Cognome: ", font= fontMod)
        self.label.grid(row=1, column=3)
        self.valoreCognome = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreCognome)
        self.entry.grid(row=1,column=4)

        self.label = tk.Label(self, text="Indirizzo: ", font= fontMod)
        self.label.grid(row=2, column=0)
        self.valoreIndirizzo = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreIndirizzo)
        self.entry.grid(row=2,column=1)

        self.label = tk.Label(self, text="C.F.: ", font= fontMod)
        self.label.grid(row=3, column=0)
        self.valoreCF = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreCF)
        self.entry.grid(row=3,column=1)

        self.label = tk.Label(self, text="Data Nascita: ", font= fontMod)
        self.label.grid(row=4, column=0)
        self.valoreDataN = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreDataN)
        self.entry.grid(row=4,column=1)

        self.label = tk.Label(self, text="Genere: ", font= fontMod)
        self.label.grid(row=5, column=0)
        # RADIOBUTTON
        self.vr = tk.IntVar(value = 0)
        self.radio1 = tk.Radiobutton(self, text='M', variable= self.vr, value= 1, command= self.radio)
        self.radio1.grid(row= 5, column= 1, sticky= tk.W)
        self.radio2 = tk.Radiobutton(self, text='F', variable=self.vr, value=2, command= self.radio)
        self.radio2.grid(row=5, column=2, sticky= tk.W)

        self.label = tk.Label(self, text="Mail: ", font= fontMod)
        self.label.grid(row=6, column=0)
        self.valoreMail = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreMail)
        self.entry.grid(row=6, column=1)

        self.label = tk.Label(self, text="Tel.: ", font= fontMod)
        self.label.grid(row=7, column=0)
        self.valoreTel = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.valoreTel)
        self.entry.grid(row=7, column=1)

        # BOTTONI
        self.button = tk.Button(self, text="Salva", command= self.salva)
        self.button.grid(row=8, column=0)

        self.button = tk.Button(self, text="Cancella", command= self.cancella)
        self.button.grid(row=8, column=1)

        self.button = tk.Button(self, text="Esci", command= self.esci)
        self.button.grid(row=8, column=2)

    def radio(self):
        if (str(self.vr.get()) == 1):
            print('M')
        else:
            print('F')


    def salva(self):
        self.lista =('{Nome: ', self.valoreNome.get() ,' Cognome: ' , self.valoreCognome.get() , ' Indirizzo: ' , self.valoreIndirizzo.get() ,
                          ' C.F.: ' , self.valoreCF.get() , ' Data Nascita: ' , self.valoreDataN.get() ,' Genere: ' , self.vr.get() ,
                          ' Mail: ' , self.valoreMail.get() ,' Tel.: ' , self.valoreTel.get() ,'}')
        file = open("C:\\Users\\Studente\\Desktop\\Elia\\Python\\FileAnagrafico", 'a')
        file.write(str(self.lista))
        file.close()


    def cancella(self):
        self.valoreNome.set("")
        self.valoreCognome.set("")
        self.valoreIndirizzo.set("")
        self.valoreCF.set("")
        self.valoreDataN.set("")
        self.vr.set(0)
        self.valoreMail.set("")
        self.valoreTel.set("")

    def esci(self):
        Finestra().quit() # chiude la finestra

if __name__ == '__main__':
    Finestra().mainloop()
