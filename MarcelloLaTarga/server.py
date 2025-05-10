from datetime import datetime
import socket  # libreria socket

hostname = '127.0.0.1'  # indirizzo IP server
portasocket = 4444  # porta ascolto
maxconnessionicoda = 5  # numero massimo di connesioni in coda
famiglia = socket.AF_INET  # socket IPv4
tipo = socket.SOCK_STREAM  # socket tipo stream
bufferdati = 1024  # dimensione max buffer dati in ricezione
serversocket = socket.socket(famiglia, tipo)  # creazione socket IP/stream
serversocket.bind((hostname, portasocket))  # lega il socket a IP/porta
serversocket.listen(maxconnessionicoda)  # attesa connessioni al socket
#
client_che_si_sono_connessi = 0
while True:  # Server live sempre in ascolto
    print("SERVER in accettazione su porta: ", portasocket)
    client_soc, indirizzo = serversocket.accept()  # accettazione connessione client
    client_che_si_sono_connessi = client_che_si_sono_connessi + 1
    print("SERVER in connessione con: ", indirizzo)
    print()
    dati_b = client_soc.recv(bufferdati)  # lettura dati dal client tramite buffer

    dati = dati_b.decode()  # decofifica oggetto bytes in oggetto stringa utf-8
    if dati:
        print("SERVER riceve: ", dati)  # dati utilizzabili

        msgServer = 'Risposta al client: ' + str(client_che_si_sono_connessi) + input('scrivi qualcosa al Client')
        print("SERVER risponde: ", msgServer)
        rispostaServer_b = msgServer.encode()

        client_soc.send(rispostaServer_b)  # echo: invio dati al client tramite buffer format bytes

    print()
    client_soc.close()  # chiusura socket client
    data_ora = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"In data {data_ora} serviti {client_che_si_sono_connessi}")  # L'f-string in Python è un modo pratico
    # per formattare le stringhe utilizzando variabili
    # direttamente all'interno delle parentesi {}
    print("----------------------------------------------")
