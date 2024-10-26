# i voti assegnati a 30 studenti di una classe sono memorizzati in un dizionario che ha come
# chiave la matricola mentre il valore associato è il voto. elenca i risultati in ordine crescente
# di voto. sucessivamente visualizza quali voti tra loro sono stati assegnati,riducendo i voti
# uguali

d = dict()  # dizionario vuoto
for i in range(3):
    matricola = int(input('inserisci Matricola: '))
    flag = True
    while flag:
        try:
            voto = float(input('inserisci voto: '))
            if voto >= 1 and voto <= 10:
                flag = False
        except ValueError:
            print('Riprova')
        d[matricola] = voto
print(d)
a = list(d.values())
print(a)
b= set(a)#trasformo la lista in un inseieme (set()) eliminando duplicati
c=list(b)#ottengo lista senza duplicati
print(c)