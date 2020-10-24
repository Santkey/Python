wiek = 18
kasa = 40

if wiek >= 18 and kasa >= 35:
    print("Możesz wejść")
elif wiek < 18:
    print("Jestes za młody")
elif kasa < 35:
    print("Masz za mało pieniędzy")

wiek1 = 13
kasa1 = 15
if not wiek1 > 12 or kasa1 >= 30:
        print("Możesz wejść")
elif wiek1 > 12:
        print("Jestes za stary")
elif kasa1 < 30:
        print("Masz za mało pieniędzy")

if (True or False) and not False:
    print("Prawda")
else:
    print("Fałsz")