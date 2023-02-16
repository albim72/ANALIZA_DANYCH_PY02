#import dane
#import dane as dn
from dane import nb as filie
from dane import book as ksiazka
from funkcje.bfunkcje import czytaj_liste, czytaj_slownik

print("__________czytanie bezpośrednie___________")

print(filie)
print(ksiazka)

print("__________czytanie za pomocą funkcji___________")
czytaj_liste(filie)
czytaj_slownik(ksiazka)
