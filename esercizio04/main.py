#quartaAI=['Mario Rossi', 'Giuseppe Verdi','Enrico Bianchi']
listaPersone=[]
persone=' '
# i='nome'
while (persone!='*'):
    persone = input('inserisci nome delle persone: ')
    listaPersone.append(persone)


fout=open('C:\\Users\\Studente\\Desktop\\mioFile.txt','w')
for i in listaPersone:
    fout.write(i+'\n')
fout.close()