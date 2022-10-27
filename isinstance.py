x = isinstance(5, int) #controlla se il valore assegnato è dello stesso tipo di quello scritto affianco

print(x) #scrive true se la correlazione è corretta, altrimenti scrive false

x = isinstance("latte", str)

print(x) 

x = isinstance("Hello", (str, float, int, str, list, dict, tuple))  #posso scrivere più tipi di variabili e se il mio oggetto è tra quelli stamperà true

print(x)

x = isinstance(8, str)

print(x)