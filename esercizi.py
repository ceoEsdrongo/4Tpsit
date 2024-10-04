#es12|72
# Input
quantitaLibri = int(input("Quanti libri della Divina Commedia vuoi acquistare? "))
prezzoUnitario = float(input("Inserisci il costo della Divina Commedia (per ogni libro): "))
aliquotaIva = float(input("Inserisci l'aliquota IVA (senza il simbolo %, ad esempio 22 per il 22%): "))

# Calcolo del prezzo totale con IVA
prezzoSenzaIva = prezzoUnitario * quantitaLibri
aliquotaDecimal = aliquotaIva / 100
prezzoConIva = prezzoSenzaIva * (1 + aliquotaDecimal)

# Output
print(f"Hai acquistato {quantitaLibri} libro/i della Divina Commedia.")
print(f"Il costo totale senza IVA è: {prezzoSenzaIva:.2f} euro.")
print(f"Il costo totale con IVA è: {prezzoConIva:.2f} euro.")


#
def ripeti_stringa():
    # Acquisisci la stringa da tastiera
    stringa = input("Inserisci una stringa: ")
    
    # Stampa la stringa su tre righe diverse
    for _ in range(3):  # Usa un ciclo for che si ripete 3 volte
        print(stringa)

# Chiamata alla funzione
ripeti_stringa()

#14|72
#Crea un programma che scriva la differenza di due numeri a e b se il loro
# prodotto è maggiore di 10 oppure la loro somma se il prodotto è minore o uguale a
# 10. Esegui poi il programma con diverse copie di valori per
# a e b: (-5, 2), (5,-5), (10, 2), (-4, -5), (5, 4), (-3,-2).

numA=int(input("inserisci il primo numero: "))
numB=int(input("inserisci il secondo numero: "))
differenza=numA-numB
prodotto=numA*numB
somma=numA+numB

if prodotto>10:
    risultato=differenza
else:
    risultato=prodotto

    print(f"numA={numA},numB={numB},risultato={risultato}")
