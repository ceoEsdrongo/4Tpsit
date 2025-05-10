import time
import tkinter
import threading


# Definizione della classe Finestra che eredita da tkinter.Frame
class Finestra(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Elementi Grafici e Thread')
        self.master.geometry('600x600')
        self.grid()
        self.crea_widgets()

    def crea_widgets(self):
        self.c1 = tkinter.Canvas(self, width=500, height=500, bg="lightyellow")
        self.c1.grid()
        self.car = self.c1.create_rectangle(10, 350, 110, 400, fill="blue")

        # Associa l'evento <KeyPress-Right> alla funzione right
        self.c1.bind("<KeyPress-Right>", self.right)

        # Associa l'evento <KeyPress-Left> alla funzione left
        self.c1.bind("<KeyPress-Left>", self.left)

        self.c1.bind("<KeyPress-Up>", self.up)
        self.c1.bind("<KeyPress-Down>", self.down)
        self.c1.bind("<KeyPress-Return>", self.rtr)

        # Il metodo focus_set() in Tkinter viene utilizzato per assegnare il focus a un widget,
        # permettendogli di ricevere gli eventi della tastiera.
        self.c1.focus_set()
    def muovisfera1(self):
        while True:
            self.c1.move(self.sfera1,0,-1)
            self.update()
            time.sleep(0.005)
            (x1,y1,x2,y2)=self.c1.coords(self.sfera1)
            if y1<=0 or y2>=500:
                self.c1.delete(self.sfera1)
                break
    def right(self, event):
        (x1, y1, x2, y2) = self.c1.coords(self.car)
        if x2 >= 500:
            pass
        else:
            self.c1.move(self.car, 20, 0)

    def left(self, event):
        (x1, y1, x2, y2) = self.c1.coords(self.car)
        if x1 <= 0:
            pass
        else:
            self.c1.move(self.car, -20, 0)

    def up(self, event):
        (x1, y1, x2, y2) = self.c1.coords(self.car)
        if y1 <= 20:
            pass
        else:
            self.c1.move(self.car, 0, -20)

    def down(self, event):
        (x1, y1, x2, y2) = self.c1.coords(self.car)
        if y2 > 480:
            pass
        else:
            self.c1.move(self.car, 0, 20)

    def rtr(self, event):
        (x1, y1, x2, y2) = self.c1.coords(self.car)
        # if self.ritieniSfera1:
        self.sfera1 = self.c1.create_oval(x1, y1, x2, y2, fill='blue')
        threading.Thread(target=self.muovisfera1).start()


if __name__ == "__main__":
    Finestra().mainloop()
