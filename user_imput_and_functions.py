username = input("Enter username:")       #permette di chiedere uno username
print("Username is: " + username)


def my_function():                        #definisce una funzione
  print("Hello from a function")

my_function()                             #serve a eseguire la funzione



def my_function(fname):                   
  print(fname + "@gmail.com")               #associa una variabile scelta a tutti i nomi

my_function("Emil")                       #gli argomenti sono tra parentisi dopo la funzione
my_function("Tobias")                     #servono ad aggiungere informazoni alla funzione
my_function("Linus")


def my_function(fname, lname):            #devo scrivere xname per ogni argomento scritto
  print(fname + " " + lname)

my_function("Emil", "Refsnes")



def my_function(*kids):                               #serve quando non so il n di elemnti contenuti nella lista
  print("The youngest child is " + kids[2])           #[2] ifa riferimento al terzo valore della lista

my_function("Emil", "Tobias", "Linus")



def my_function(child3, child2, child1):                   #normalmente sono in ordine ma posso abbinare i nomi a xvariabile (parametri) per metterli nell'ordine che voglio
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def my_function(**kid):                                   #kid["lname"] dizionario    lname chiave valore
  print("His last name is " + kid["pippo"])

my_function(fname = "Tobias", lname = "Refsnes", pippo = "pluto")



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")                         #se non specifico il nome mi stampa quello definito in def my_function(country = "Norway"):
my_function("India")
my_function()
my_function("Brazil")



def my_function(food):
  for x in food:                                  #serve a stampare una lista
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def testfunc(x):
  if x=='pippo': return 'ciao'
  else: return 'arrivederci'


print(testfunc('z'))

def my_function(x):
  return 5 * x                                  #return è ciò che la funzione da in uscita in base a ciò che gli inserisci

print(my_function(3))
print(my_function(5))
print(my_function(9))



def myfunction():
  pass



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)
