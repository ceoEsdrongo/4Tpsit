import socket                                   # importa la libreria socket
clientsocket = socket.socket()                  # creazione socket di nome clientsocket
hostname = '127.0.0.1'                          # indirizzo IP server ECHO
portasocket = 4444                              # porta connessione
bufferdati = 1024                               # dimensione max buffer dati ricezione
clientsocket.connect((hostname,portasocket))    # connessione al server in ascolto
print ("CLIENT")
messaggio = " - Invio dati client."
#
print ("CLIENT genera:\n ", messaggio)          # formato bytes
dati_b = messaggio.encode()                     # codifica utf-8 oggetto stringa in oggetto bytes
print ("CLIENT invia:\n ", dati_b)              # formato bytes
print ()
try:
    clientsocket.send(dati_b)                       # invio dati al server ECHO
    datiricevuti_b = clientsocket.recv(bufferdati)  # ricezione dati dal server ECHO in formato bytes
    print ("CLIENT riceve dal server l'echo:\n", datiricevuti_b)
    #
    datiricevuti = datiricevuti_b.decode()          # decodifica oggetto bytes in oggetto stringa utf-8
    print ("CLIENT utilizza:",datiricevuti)         # dati utilizzabili
    #
# Gestione errori
#
except socket.error as e:
    print ("Socket errore: %s" %str(e))   # metodo vecchio di formattazione delle stringhe in Python,
                                          # noto come string interpolation con %
except Exception as e:
    print (f"Altra eccezione: {e}")       # L'f-string in Python è un modo pratico
                                          # per formattare le stringhe utilizzando variabili
                                          # direttamente all'interno delle parentesi {}
finally:
    clientsocket.close()                            # chiusura socket client
    print ()
    print ("Client chiude connessione")

