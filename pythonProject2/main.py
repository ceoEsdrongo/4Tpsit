
flag = True
cont = 0
lista = [1, 2, 3]
listd = [{'Nome': 'Mario', 'Cognome': 'Rossi', 'mail': False}, \
         {'Nome': 'Giuseppe', 'Cognome': 'Verdi', 'mail': False}]
print('scegli 1 per la prenotazione, 2 per la visualizazzione: ')
if int(input('digita il numero: ')) == 1:
    while True:
        try:
            Cognome = input('inserisci il cognome: ')
            nome = input('inserisci il nome: ')
            # telefono=1234
            # indirizzo='aaaa'
            # CF='a'
            mail = False
            listd.append({'Nome': nome, 'Cognome': Cognome, 'mail': mail})
        except KeyboardInterrupt:
            print('Control+C')
            flag = False
else:
    for i in range(0, len(listd)):
        print(i)
    for c in i.keys():
        print(c)
        print('chiave= ', c, 'valore', 'valore= ', i[c])

fout = open('C:\\Users\\Studente\\Desktop\\pythonProject2\\a.txt', 'w')  # usare append per sovrascrivere
for i in listd:
    fout.write(str(i))
    fout.close
fin = open('C:\\Users\\Studente\\Desktop\\pythonProject2\\a.txt', 'r')
print('lettura file')
parola = fin.readLine()
print(parola)
fin.close
