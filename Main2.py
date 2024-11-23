from main import inserimento

lista =[]
flag= True
#controllo inserimento dati
for i in range(20):
    while flag:
        inserimento=input('inserisci il cognome_nome (l\'inserimento termina con /): ')
        if inserimento=='*':
            flag=False
        else:
            lista.append(inserimento)
print(lista)


fout=open('C:\\Users\\Studente\\Desktop\\esercizi23-11-2024','w')
fout.write(str(lista))
fout.close()