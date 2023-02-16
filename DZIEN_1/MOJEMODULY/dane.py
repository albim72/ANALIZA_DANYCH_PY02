class Book:
    #deklaracja stanu(dane) -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=25):
        self.idksiazki = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #zachowanie -> funkcje klasy -> metody
    def create_book(self):
        print("utworzono nową książkę!  ")

    def print_book(self):
        print(f"książka: {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}")

    def rabat(self,procent):
        return self.cena*procent/100

    def setcena(self,nowacena):
        self.cena = nowacena

b1 = Book(32,"Wiedźmin","Andrzej Sapkowski",38)
b1.print_book()
print(f'rabat od ceny: {b1.cena} zł wynosi {b1.rabat(7.5):.2f} zł')

print("zmiana ceny")
b1.setcena(52)
b1.print_book()
print(f'rabat od ceny: {b1.cena} zł wynosi {b1.rabat(7.5):.2f} zł')

b2 = Book(46,"Hobbit","J.R.R Tolkien",43)
b2.print_book()
print(f'rabat od ceny: {b2.cena} zł wynosi {b2.rabat(11):.2f} zł')

b3 = Book(66,"ABC Kulturysty","John Brown")
b3.oprawa = "twarda"
b3.print_book()





