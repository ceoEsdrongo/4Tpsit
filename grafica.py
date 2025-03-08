import tkinter as tk
from tkinter.font import Font

class Esempio(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('GAME')
        self.master.geometry('600x600')
        self.grid()
        self.crea_widgets()

    def crea_widgets(self):
        fontMod = Font(family="Calibri", size=14)

        # Bottoni per spostare la palla
        self.sinistra = tk.Button(self, text='<-', command=self.sx, fg="red", bg="lightcyan", font=fontMod)
        self.sinistra.grid(row=1, column=0)

        self.destra = tk.Button(self, text='->', command=self.dx, fg="red", bg="lightcyan", font=fontMod)
        self.destra.grid(row=1, column=2)

        self.sopra = tk.Button(self, text='˄', command=self.up, fg="red", bg="lightcyan", font=fontMod)
        self.sopra.grid(row=0, column=1)

        self.sotto = tk.Button(self, text='˅', command=self.dw, fg="red", bg="lightcyan", font=fontMod)
        self.sotto.grid(row=2, column=1)

        # Bottone per uscire
        self.pulsante2 = tk.Button(self, text='Esci', command=self.master.destroy, fg="red", bg="lightcyan", font=fontMod)
        self.pulsante2.grid(row=2, column=3)

        # Canvas per disegnare la palla
        self.c1 = tk.Canvas(self, width=300, height=300, bg="yellow")
        self.c1.bind('<Enter>', self.colora)
        self.c1.bind('<Leave>', self.scolora)
        self.ball = self.c1.create_oval(50, 50, 100, 100, fill="blue")
        self.c1.grid(row=3, column=1, padx=20, pady=20)  # Spazio tra gli elementi
        self.master.bind('<KeyPress-Left>', self.l)

    def colora(self, event):
        self.c1.config(bg='blue')
    def scolora(self, event):
        self.c1.config(bg='red')

    def sx(self):
        x1, y1, x2, y2 = self.c1.coords(self.ball)
        if x1 > 0:
            self.c1.move(self.ball, -10, 0)

    def l(self, event):
        x1, y1, x2, y2 = self.c1.coords(self.ball)
        if x1 > 0:
            self.c1.move(self.ball, -10, 0)

    def dx(self):
        x1, y1, x2, y2 = self.c1.coords(self.ball)
        if x2 < 300:
            self.c1.move(self.ball, 10, 0)

    def up(self):
        x1, y1, x2, y2 = self.c1.coords(self.ball)
        if y1 > 0:
            self.c1.move(self.ball, 0, -10)

    def dw(self):
        x1, y1, x2, y2 = self.c1.coords(self.ball)
        if y2 < 300:
            self.c1.move(self.ball, 0, 10)

if __name__ == '__main__':
    Esempio().mainloop()

