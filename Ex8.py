lista = ["Chcę","nauczyć", "się", "programowania", ]

i = 0
while i < len(lista): #dopóki i jest mniejsza od długości listy
    print(lista[i]) # wypisuj i
    i += 1 # inkrementuj i

for x in lista: # dla x w liście
    print(x) # wypisz x

print(list(range(10))) #wypisz listę w zakresie 10

for y in range(1, 11, 2): #1el to początek, 2 el to koniec, 3 el to skok
    print(y) # wypisz liczby od 0 do  9