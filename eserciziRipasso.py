# creare una lista contenente 20 interi random in [0, 100) e stampare il
# numero di elementi pari,il numero di elementi maggiori di 70,
# media e varianza degli elementi;

#import random
#
# varianza = 0
# somma = 0
# numeri = list()
# for i in range(20):
#     rnd = random.randint(0, 100)
#     numeri.append(rnd)
#     if rnd > 70:
#         print("Questo numero è maggiore di 70", rnd)
#
#     if rnd % 2 == 0:
#         print("il numero", rnd, "è pari")
#     else:
#         print("il numero", rnd, "è dispari")
#     somma += rnd
#     if varianza < rnd:
#         varianza = rnd - varianza
#
#     elif varianza > rnd:
#         varianza = varianza - rnd
#
# media = somma / len(numeri)
#
# print(media)

#   leggere da tastiera una sequenza di interi (la lunghezza
#   è data anch'essa da tastiera), memorizzarla in una lista,
#   verificare se la sequenza è in ordine non decrescente;
# n = int(input("Inserisci la quantità di numeri da inserire: "))
# lista = list()
# for i in range(n):
#     numeri = int(input("inserisci i numeri da inserire: "))
#     lista.append(numeri)
# bSort = lista
# bSort.sort(reverse=True)
# dec=lista
# dec.sort()
# if lista != bSort:
#     print("la lista non è in ordine decrescente")
# elif lista == bSort:
#     print("la lista è decrescente")
# elif lista != dec and lista != bSort:
#     print("la lista non è crescente o decrescente")
# elif lista == dec:
#     print("la lista è crescente")

# modificare il programma precedente per verificare se la sequenza è crescente,
# non decrescente, non crescente o decrescente


#data una lista di interi, creare un altra lista contenente
# solo gli elementi di posizione pari della prima lista
# import random
# pari=list()
# interi=list()
# dispari=list()
# n=int(input("inserire una quantità di numeri"))
# for i in range(n):
#     numero=random.randint(1,100)
#     interi.append(numero)
#     if i %2==0:
#         pari.append(numero)
#     elif i%2!=0:
#         dispari.append(numero)
# print(interi)
# print(pari)
# print(dispari)
#data una lista di interi, creare un altra
# lista contenente solo gli elementi di posizione dispari della prima lista

# data una lista di interi, creare un altra lista contenente solo gli elementi pari
# (deve essere pari il valore, indipendentemente dalla posizione) della prima lista





