x = 12
y = 0

try:
    lista = [] #pusta lista
    print(lista[0]) #wypisz piewrszy indeks z listy
    print(x + "!") #dodawanie dwóch wartości o różnych typach znaku
    print(x / y)
    print("Ostatnia linijka")

except (ZeroDivisionError, TypeError): #wyjątki dzielenie przez 0 i typu pisowni
    print("Wyjątek: Jeden z 3 błędów")
except: #każdy inny wyjątek nieprzewidziany wcześniej
    print("Inny rodzaj wyjątku")
finally: # ostateczna komenda po każdym z przypadków
    print("Dalsze instrukcje...")