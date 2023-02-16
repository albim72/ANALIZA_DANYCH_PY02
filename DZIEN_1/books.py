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
        
