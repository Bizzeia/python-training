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

#es alberi
def ast(lista):
 for x in lista:
        print("*" * x)
lista = []
numeri = int(input("Quanti numeri: "))
for t in range(numeri):
        nn = int(input("inserisci numero: "))
        lista.append(nn)
ast(lista)

#albero di natale 

h = int(input("altezza: "))
def alb(h):
    spazi = h-1
    ast = h
    for x in range(0,h):
        print(spazi * " ",ast * "*")
        ast = ast + 2
        spazi = spazi -1
alb(h)

#esercizio J
#Definisci una funzione che calcoli il Massimo comun divisore tra una lista di numeri ricevuta in input

def primo(y):
    for x in range(2,y):
        check = int(y/x)
        if check * x == y:
            return False
    return True

y = int(input("inserisci un numero: "))
print(primo(y))



#esercizio K

num1 = int(input("scrivere un numero: "))
num2 = int(input("scrivere un numero: "))

def bommo (free, fro):
    if num1>num2:
        for prova in range(num1, 10000000000)
            if prova%num1 == 0 and prova%num2 == 0:
                print(prova)
                break
    if num1<num2:
        for prova2 in range(num2, 10000000000):
            if prova2%num2 == 0 and prova2%num1 == 0:
                print (prova2)
                break
    if num1 == num2
        print("bisogna inserire due numeri diversi ")

bommo(num1,num2)

