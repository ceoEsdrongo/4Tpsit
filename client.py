import socket
# Importa il modulo socket per la comunicazione di rete tramite socket TCP/IP.

DIM = 20
# Definisce la dimensione della griglia (20x20).

def crea_griglia():
    return [["." for _ in range(DIM)] for _ in range(DIM)]
# Funzione che crea e ritorna una griglia 20x20 inizializzata con "." (punti),
# rappresentando caselle vuote.

def stampa_griglia(griglia):
    print("\n     " + " ".join(f"{i:2}" for i in range(DIM)))
    # Stampa l'intestazione delle colonne numerate da 0 a 19, con spaziatura di 2 caratteri.
    print("   +" + "---" * DIM + "+")
    # Stampa una riga orizzontale di separazione sopra la griglia.
    for y in range(DIM):
        riga = f"{y:2} | " + " ".join(f"{c:2}" for c in griglia[y]) + " |"
        # Per ogni riga y, stampa il numero di riga seguito dal contenuto delle celle,
        # allineate con spaziatura di 2 caratteri, delimitate da barre verticali.
        print(riga)
    print("   +" + "---" * DIM + "+")
    # Stampa una riga orizzontale di chiusura sotto la griglia.

griglia_visibile = crea_griglia()
# Crea la griglia visibile per il giocatore, inizialmente tutta vuota (".").

while True:
    stampa_griglia(griglia_visibile)
    # Stampa la griglia aggiornata prima di ogni mossa.

    try:
        x = int(input("Inserisci X (0-19): "))
        y = int(input("Inserisci Y (0-19): "))
        # Chiede all'utente di inserire le coordinate X e Y della cella da colpire.
        if not (0 <= x < DIM and 0 <= y < DIM):
            print("Coordinate fuori dalla griglia!")
            continue
        # Controlla che le coordinate siano valide (all'interno della griglia).
    except ValueError:
        print("Coordinate non valide.")
        continue
        # Gestisce errori di inserimento non numerico.

    clientsocket = socket.socket()
    # Crea un socket TCP/IP.
    clientsocket.connect(("127.0.0.1", 4444))
    # Connette il socket al server locale sulla porta 4444.
    messaggio = f"{x},{y}"
    clientsocket.send(messaggio.encode())
    # Invia al server il messaggio con le coordinate scelte, codificato in bytes.

    risposta = clientsocket.recv(1024).decode()
    # Riceve la risposta dal server (fino a 1024 byte) e la decodifica in stringa.
    clientsocket.close()
    # Chiude la connessione socket.

    # La risposta è del tipo:
    # "Colpito! Affondata nave P. | CPU colpisce (x,y): colpito!"
    risposte = risposta.split(" | ")
    # Divide la risposta in due parti separate da " | ",
    # la prima relativa all'esito della mossa del giocatore, la seconda all'azione CPU.
    esito_tuo_colpo = risposte[0]
    esito_cpu = risposte[1] if len(risposte) > 1 else ""
    # Assegna i risultati alle rispettive variabili.

    print("Risposta dal server:", esito_tuo_colpo)
    # Mostra all'utente l'esito del suo colpo.
    if "Colpito" in esito_tuo_colpo:
        griglia_visibile[y][x] = "X"
        # Se il colpo è andato a segno, aggiorna la griglia con "X" sulla cella.
    elif "Acqua" in esito_tuo_colpo:
        griglia_visibile[y][x] = "O"
        # Se il colpo ha mancato, aggiorna la griglia con "O" sulla cella.

    if esito_cpu:
        print("Mossa CPU:", esito_cpu)
        # Se presente, stampa la mossa fatta dalla CPU.

    if "Hai vinto" in esito_tuo_colpo or "Hai perso" in esito_cpu:
        print("\nPartita terminata.")
        stampa_griglia(griglia_visibile)
        break
        # Se il gioco è terminato (vittoria o sconfitta), stampa messaggio,
        # mostra la griglia finale e interrompe il ciclo (termina il gioco).
