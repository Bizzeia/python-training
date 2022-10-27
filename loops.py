inter = ["Onana", "Gosens", "Brozovic"]   #creo una lista 
for x in inter:   #stampa gli elementi di una lista un colonna
  print(x) 

for x in "bommosium":  #stampa in colonna tutte le lettere di una parola
  print(x) 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":   #appena arriva a una parola determinata si blocca
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  #appena arriva a banan stampa tutte le cose prima, banana esclusa
    break
  print(x) 

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  #appena arrivata ad una parola specifica la salta e stampa quelle dopo
    continue
  print(x) 

for x in range(6): 
  print(x)  #stampa tutti i numeri fino a quello determinato, escludendo quello stesso 

for x in range(2, 6): 
  print(x)   #stampa tutti i numeri tra quelli determinati

for x in range(2, 30, 3):
  print(x)   #stampo i numeri compresi tra 2 e 30, ma solo distanti di 3 unità

for x in range(6):
  print(x) #stampo i numeri fino a 6
else:
  print("Finally finished!") #appena arrivato al numero finale stampo la stringa

for x in range(6):
  if x == 3: break 
  print(x)
else:
  print("Finally finished!") #non stamperà mai la stringa perchè il break non permette di arrivare all'ultimo numero

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:  #associa in ordine ciascun elemento nella prima parentesi ad un altro nella seconda parentesi
    print(x, y)

for x in [0, 1, 2]:
    pass    #inserisco pass per non ricevere errore, se ho dei loop vuoti

esercizio 5 


import random  #con il comando random sceglie un numero a caso tra il range scelto

print(random.randrange(1, 10))