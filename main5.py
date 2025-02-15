import tkinter as tk
from tkinter.font import Font


class Esempio(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('GAME')
        self.master.geometry('600x600')
        self.x = 0
        self.y = 0

        self.grid()
        self.listaAnagrafica = []
        self.crea_widgets()

    def crea_widgets(self):
        fontMod = Font(family="Calibri", size=14)

        self.sx = tk.Button(self, text='<-', command=self.sx, fg="red", bg="lightcyan", font=fontMod)
        self.sx.grid(row=1, column=0)
        self.dx = tk.Button(self, text='->', command=self.dx, fg="red", bg="lightcyan", font=fontMod)
        self.dx.grid(row=1, column=2)
        self.up = tk.Button(self, text='|', command=self.up, fg="red", bg="lightcyan", font=fontMod)
        self.up.grid(row=0, column=1)
        self.dw = tk.Button(self, text='|', command=self.dw, fg="red", bg="lightcyan", font=fontMod)
        self.dw.grid(row=2, column=1)

        self.pulsante2 = tk.Button(self, text='Esci', command=self.master.destroy, fg="red", bg="lightcyan",
                                   font=fontMod)
        self.pulsante2.grid(row=2, column=4)

        self.c1 = tk.Canvas(self, width=200, height=700, bg="yellow")
        self.c1.grid(row=10, column=4)
        self.ball = self.c1.create_oval(50, 10, 150, 110, fill="blue")

    def sx(self):
        self.x -= 10
        self.c1.create_oval(50 + self.x, 10, 150 + self.x, 110, fill="blue")

    def dx(self):
        self.x += 10
        self.c1.create_oval(50 + self.x, 10, 150 + self.x, 110, fill="blue")

    def up(self):
        self.y -= 10
        self.c1.create_oval(50, 10 + self.y, 150, 110 + self.y, fill="blue")

    def dw(self):
        self.y += 10
        self.c1.create_oval(50, 10 + self.y, 150, 110 + self.y, fill="blue")

    def sx(self):
        (x1, y1, x2, y2) = self.c1.coords(self.ball)
        if x1 >= 10:
            self.x -= 10
            self.y = 0
            self.c1.move(self.ball, self.x, self.y)

    def dx(self):
        self.x += 10
        self.y = 0
        self.c1.move(self.ball, self.x, self.y)

    def up(self):
        self.x = 0
        self.y -= 10
        self.c1.move(self.ball, self.x, self.y)

    def dw(self):
        self.x = 0
        self.y += 10
        self.c1.move(self.ball, self.x, self.y)


if __name__ == '__main__':
    Esempio().mainloop()
