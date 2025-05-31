import socket
import random

DIM = 20  # Dimensione della griglia 20x20

# Funzione per creare una griglia vuota piena di "."
def crea_griglia():
    return [["." for _ in range(DIM)] for _ in range(DIM)]

# Funzione per stampare la griglia in modo leggibile sulla console
def stampa_griglia(griglia):
    print("\n     " + " ".join(f"{i:2}" for i in range(DIM)))
    print("   +" + "---" * DIM + "+")
    for y in range(DIM):
        riga = f"{y:2} | " + " ".join(f"{c:2}" for c in griglia[y]) + " |"
        print(riga)
    print("   +" + "---" * DIM + "+")

# Funzione per piazzare navi casualmente (usata per la CPU)
def piazza_navi(griglia):
    # Navi da piazzare: tipo e lunghezze (es. due navi piccole di 1 cella)
    navi_da_piazzare = {
        "P": [1, 1],          # 2 navi piccole (1 cella)
        "M": [2],             # 1 nave media (2 celle)
        "G": [2, 2],          # 2 navi grandi (2 celle)
    }
    navi_posizionate = {}  # Dizionario con coordinate e info nave

    for tipo, lunghezze in navi_da_piazzare.items():
        for lunghezza in lunghezze:
            posizionata = False
            # Prova a piazzare la nave finché non trova una posizione valida
            while not posizionata:
                orientamento = random.choice(["orizzontale", "verticale"])
                if orientamento == "orizzontale":
                    y = random.randint(0, DIM - 1)
                    x = random.randint(0, DIM - lunghezza)
                    coordinate = [(y, x + i) for i in range(lunghezza)]
                else:
                    y = random.randint(0, DIM - lunghezza)
                    x = random.randint(0, DIM - 1)
                    coordinate = [(y + i, x) for i in range(lunghezza)]

                # Controlla se tutte le celle sono libere "."
                if all(griglia[yy][xx] == "." for yy, xx in coordinate):
                    # Piazza la nave
                    for yy, xx in coordinate:
                        griglia[yy][xx] = tipo
                        navi_posizionate[(yy, xx)] = (tipo, tuple(coordinate))
                    posizionata = True
    return griglia, navi_posizionate

# Funzione per piazzare le navi del giocatore in posizioni fisse (non random)
def piazza_navi_fisse(griglia):
    navi_posizionate = {}

    # 2 navi piccole (P) 1 cella
    posizioni_p = [(0,0), (2,2)]
    for y, x in posizioni_p:
        griglia[y][x] = "P"
        navi_posizionate[(y, x)] = ("P", ((y,x),))

    # 1 nave media (M) 2 celle orizzontale
    y, x = 5, 5
    coordinate_m = [(y, x), (y, x+1)]
    for yy, xx in coordinate_m:
        griglia[yy][xx] = "M"
        navi_posizionate[(yy, xx)] = ("M", tuple(coordinate_m))

    # 2 navi grandi (G) 2 celle verticali
    y1, x1 = 10, 10
    coordinate_g1 = [(y1, x1), (y1+1, x1)]
    for yy, xx in coordinate_g1:
        griglia[yy][xx] = "G"
        navi_posizionate[(yy, xx)] = ("G", tuple(coordinate_g1))

    y2, x2 = 15, 15
    coordinate_g2 = [(y2, x2), (y2+1, x2)]
    for yy, xx in coordinate_g2:
        griglia[yy][xx] = "G"
        navi_posizionate[(yy, xx)] = ("G", tuple(coordinate_g2))

    return griglia, navi_posizionate

# Funzione per controllare se tutte le navi sono affondate
def tutte_affondate(navi_affondate, navi_posizionate):
    # Raccogli tutte le coordinate delle navi in un set
    navi_totali = set()
    for _, (_, coord) in navi_posizionate.items():
        navi_totali.add(coord)
    # Verifica se tutte le coordinate delle navi sono in quelle affondate
    return navi_affondate == navi_totali

# --- Setup iniziale ---

# Navi CPU random
griglia_cpu = crea_griglia()
griglia_cpu, navi_cpu = piazza_navi(griglia_cpu)
griglia_visibile_cpu = crea_griglia()

# Navi giocatore fisse (così il giocatore sa dove sono)
griglia_giocatore = crea_griglia()
griglia_giocatore, navi_giocatore = piazza_navi_fisse(griglia_giocatore)
griglia_visibile_giocatore = crea_griglia()

# Celle già colpite da giocatore (sulla CPU) e da CPU (sul giocatore)
celle_colpite_cpu = set()
celle_colpite_giocatore = set()

# Navi affondate per CPU e giocatore
navi_cpu_affondate = set()
navi_giocatore_affondate = set()

# Setup socket server TCP
serversocket = socket.socket()
serversocket.bind(("127.0.0.1", 4444))
serversocket.listen(1)

print("SERVER in attesa su porta 4444...")

# Loop principale del gioco (continua finché non vince qualcuno)
while True:
    client, addr = serversocket.accept()  # Accetta connessione client
    print("\nConnessione da:", addr)
    dati = client.recv(1024).decode()  # Riceve coordinate dal client
    if dati == "*":  # Se riceve "*" chiude la partita
        client.close()
        break

    try:
        x, y = map(int, dati.split(","))  # Estrae coordinate colpo
        print(f"Colpo ricevuto dal giocatore in ({x}, {y})")

        # --- MOSSA GIOCATORE SU CPU ---
        if (y, x) in celle_colpite_cpu:
            risposta = "Hai già colpito qui!"
        else:
            celle_colpite_cpu.add((y, x))
            cella = griglia_cpu[y][x]

            if cella in ["P", "M", "G"]:
                tipo, coordinate = navi_cpu[(y, x)]
                griglia_visibile_cpu[y][x] = "X"  # Segna colpito
                griglia_cpu[y][x] = "."          # Rimuove pezzo nave
                # Controlla se nave intera affondata
                if all(c in celle_colpite_cpu for c in coordinate):
                    if coordinate not in navi_cpu_affondate:
                        navi_cpu_affondate.add(coordinate)
                        risposta = f"Colpito! Affondata nave {tipo}."
                    else:
                        risposta = "Colpito di nuovo su nave già affondata."
                else:
                    risposta = "Colpito!"
            else:
                griglia_visibile_cpu[y][x] = "O"  # Segna acqua
                risposta = "Acqua."

        # Controlla se giocatore ha vinto
        if tutte_affondate(navi_cpu_affondate, navi_cpu):
            risposta += " | Hai affondato tutte le navi CPU. Hai vinto!"

        # --- MOSSA CPU SU GIOCATORE (se il giocatore non ha ancora vinto) ---
        risposta_cpu = ""
        if "Hai vinto" not in risposta:
            # CPU sceglie coordinate random non colpite ancora
            while True:
                y_cpu = random.randint(0, DIM - 1)
                x_cpu = random.randint(0, DIM - 1)
                if (y_cpu, x_cpu) not in celle_colpite_giocatore:
                    break
            celle_colpite_giocatore.add((y_cpu, x_cpu))
            cella_cpu = griglia_giocatore[y_cpu][x_cpu]

            if cella_cpu in ["P", "M", "G"]:
                tipo_cpu, coord_cpu = navi_giocatore[(y_cpu, x_cpu)]
                griglia_visibile_giocatore[y_cpu][x_cpu] = "X"
                griglia_giocatore[y_cpu][x_cpu] = "."
                if all(c in celle_colpite_giocatore for c in coord_cpu):
                    if coord_cpu not in navi_giocatore_affondate:
                        navi_giocatore_affondate.add(coord_cpu)
                        risposta_cpu = f"CPU colpisce ({x_cpu},{y_cpu}): affondata nave {tipo_cpu}."
                    else:
                        risposta_cpu = f"CPU colpisce ({x_cpu},{y_cpu}): colpito di nuovo su nave affondata."
                else:
                    risposta_cpu = f"CPU colpisce ({x_cpu},{y_cpu}): colpito!"
            else:
                griglia_visibile_giocatore[y_cpu][x_cpu] = "O"
                risposta_cpu = f"CPU colpisce ({x_cpu},{y_cpu}): acqua."

            # Controlla se CPU ha vinto
            if tutte_affondate(navi_giocatore_affondate, navi_giocatore):
                risposta_cpu += " | CPU ha affondato tutte le tue navi. Hai perso!"

        # Manda risposta completa al client (giocatore)
        risposta_completa = risposta
        if risposta_cpu:
            risposta_completa += " | " + risposta_cpu

        client.send(risposta_completa.encode())

        # Stampa griglie per debug sul server
        print("Griglia CPU visibile (dal giocatore):")
        stampa_griglia(griglia_visibile_cpu)
        print("Griglia Giocatore visibile (dal CPU):")
        stampa_griglia(griglia_visibile_giocatore)

    except Exception as e:
        client.send(f"Errore nei dati: {e}".encode())

    client.close()

serversocket.close()
print("Server chiuso.")
