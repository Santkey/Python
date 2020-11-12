def dzielenie(x, y): #funkcja dzielenie z x i y
    assert y != 0, " Y == 0" #assert sprawdza czy zachodzie True czy False
    # w przypadku true nic nie robi, przy false zwraca assertion error
    if y == 0: #jeżeli y = 0
        raise ZeroDivisionError("Dzielenie przez zero!") #podnieś error: dzielenie przez zero
    print(x / y)


try: #spróbuj wykonać
    dzielenie(4, 0)
except ZeroDivisionError: #wyjątek: dzielenie przez zero
    print("Błąd")
    raise # podnieś wyjątek jeżeli wystąpi błąd


