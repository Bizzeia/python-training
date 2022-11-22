#esercizio A
print("esercizio A")

def my_function():
    numero = input("Scrivi un numero:")
    print(numero)

for x in range(5):
    my_function()

    

#esercizio B
print("esercizio B")

elenconumeri = []

def my_function2():
    numero = input("Scrivi un numero:")
    elenconumeri.append(numero)

for x in range(5):
    my_function2()

elenconumeri.reverse()
print(elenconumeri)


#esercizio C
print("esercizio C")

elenco = []
elencopari = []

def my_function3():
    numero = input("Scrivi un numero:")
    elenco.append(numero)

for x in range(5):
    my_function3()

for n in elenco:
    check = int(n/2)
    if (check * 2) == n: 
        elencopari.append(n)

elencopari.reverse()
print(elenco)


#esercizio D
print("esercizio D")

y = int(input("Quanti numeri devo stampare: "))
lista = []
for x in range(y):
    k = int(input(" Numero da inserire: "))
    print (pow(k,2))