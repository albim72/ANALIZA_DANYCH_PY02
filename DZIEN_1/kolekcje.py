#krotka
miasta = ("Kraków","Lublin","Warszawa","Poznań","Wrocław","Kraków","Gdańsk")
print(miasta)
print(miasta[2:7])
print(miasta.count("Kraków"))

#zbiór

kolory = {"zielony","biały","niebieski","fioletowy","żółty","czerwony","zielony"}
print(kolory)
print(kolory)
print(kolory)

kolory.add("czarny")
print(kolory)
kolory.update(["magenta","cyan","brąz"])
print(kolory)

liczby = [3,67,8,3,13,4,5,6,2,3,4,78,4,24,6,4,2,3]

lbset = set(liczby)
liczby = list(lbset)
print(sorted(liczby))

#słownik

osoba = {
    "imię":"Jan",
    "nazwisko":"Kot",
    "miasto":"Toruń",
    "wiek":45,
    888:687888
}

print(osoba)
print(osoba["miasto"])
print(osoba[888])

osoba.pop(888)
print(osoba)

osoba["kolor oczu"] = "niebieski"
print(osoba)

print(osoba.items())
print(osoba.keys())
print(osoba.values())
