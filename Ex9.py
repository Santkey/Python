def funkcja_test(): #stworzenie funkcji
    print("Funkcja!") #wypisanie funkcji

funkcja_test() # wywołanie funkcji

def dodaj(x): #stworzenie funkcji
    print(x + 1)#wypisanie

zmienna = dodaj(2)
print(zmienna)

def dodaj(x, y = 1, z = 0): #stworzenie funkcji
    return x + y + z #wypisanie

print(dodaj(2, 3, 5)) #wywołanie z podaniem wartości
wynik = dodaj(2, 3, 5)
print(wynik)