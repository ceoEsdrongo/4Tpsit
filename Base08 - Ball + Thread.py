import tkinter as tk
import threading
import time


class Finestra(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Due Sfere")
        self.geometry("400x400")

        self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canvas.pack()

        # Creazione delle sfere
        self.sfera1 = self.canvas.create_oval(50, 50, 100, 100, fill='red')
        self.sfera2 = self.canvas.create_oval(150, 50, 200, 100, fill='blue')

        # Velocità delle sfere
        self.velocita1_x = 1
        self.velocita1_y = 0
        self.velocita2_x = 0
        self.velocita2_y = 1

        # Avvio dei thread
        threading.Thread(target=self.muovi_sfera1, daemon=True).start()
        threading.Thread(target=self.muovi_sfera2, daemon=True).start()

    def muovi_sfera1(self):
        while True:
            self.canvas.move(self.sfera1, self.velocita1_x, self.velocita1_y)
            pos = self.canvas.coords(self.sfera1)
            # Controlla se la sfera 1 ha raggiunto il bordo destro o sinistro
            if pos[2] >= 400 or pos[0] <= 0:
                self.velocita1_x = -self.velocita1_x  # Inverti la direzione orizzontale
            # Controlla se la sfera 1 ha raggiunto il bordo superiore o inferiore
            if pos[3] >= 400 or pos[1] <= 0:
                self.velocita1_y = -self.velocita1_y  # Inverti la direzione verticale
            self.update()
            time.sleep(0.005)  # Ritardo per rallentare il movimento

    def muovi_sfera2(self):
        while True:
            self.canvas.move(self.sfera2, self.velocita2_x, self.velocita2_y)
            pos = self.canvas.coords(self.sfera2)
            # Controlla se la sfera 2 ha raggiunto il bordo destro o sinistro
            if pos[2] >= 400 or pos[0] <= 0:
                self.velocita2_x = -self.velocita2_x  # Inverti la direzione orizzontale
            # Controlla se la sfera 2 ha raggiunto il bordo superiore o inferiore
            if pos[3] >= 400 or pos[1] <= 0:
                self.velocita2_y = -self.velocita2_y  # Inverti la direzione verticale
            self.update()
            time.sleep(0.005)  # Ritardo per rallentare il movimento


if __name__ == "__main__":
    Finestra().mainloop()
