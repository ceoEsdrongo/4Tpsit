#creare undizionario con i dati anagrafici e salvare i datianche su un file

dizionario ={}
flag =True

while flag:
    inserimento=input('inserisci cognome (l\'inserimento termina con *): ')
    if inserimento =='*':
        flag= False
    else:
        Cognome=inserimento
        flagCognome=True
        for i in dizionario.keys():
            if  i == Cognome:
                print('cognome già esistente')
                flagCognome=False
        Rif_Cognome=Cognome
        if flagCognome:
            Nome=input('inserisci nome: ')
            Tel=int(input('inserisci tel: '))
            indirizzo = input('inserisci indirizzo ')
        dizionario[Rif_Cognome]=[Nome, Tel,indirizzo]
print(dizionario)