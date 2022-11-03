#Riempi una lista di 5 numeri e stampa il minore.

import random 

elenco = []

for x in range(5):
    n = random.randrange(0,777)
    elenco.append(n)

z = elenco[0]

for y in elenco:
    if y < z:
        z = y 

print(elenco)
print("minore")
print(z)

#Dichiara due liste. Una con nomi di animali e l’altra con numeri. Aggiungi tutti gli elementi della seconda lista alla prima.
#Stampa soltanto i numeri maggiori di 5

animali = ["cane", "gatto", "gallo"]
animali.reverse()
print (animali)

#Dichiara due liste. Una con nomi di animali e l’altra con numeri. Aggiungi tutti gli elementi della seconda lista alla prima.
#Stampa soltanto i numeri maggiori di 5

animali = ["tgtg", "egeg", "erfw", "sdjg", "rgf"]
numeri = [233, 51, 45, 56, 87]

print(animali + numeri)

f

for x in numeri:
    if x > 5:
        print(x)

#Riempi una lista di 10 numeri casuali (utilizza un ciclo for) e stampa solo i numeri pari
import random 
lista = []


for x in range(10):
    rnd = random.randrange(0,3542)
    lista.append(rnd)

print("num pari")

for n in lista:
    check = int(n/2)
    if (check * 2) == n: 
        print(n)