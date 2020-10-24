from random import randint
los = randint(1,100) #los z przedziału 1 do 100
odp =  -1 # aby liczba wykraczała poza podany przedział
i = 0 #liczba zgadnięć
print("Zgadnij liczbę z przedziału (1 do 10)")
while odp != los:
    i += 1 #dodaj liczbę zgadnięć
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Niestety, liczba jest mniejsza")
    elif odp < los:
        print("Niestety, liczba jest większa")
print("Brawo, wygrałeś za", i, "razem.")
