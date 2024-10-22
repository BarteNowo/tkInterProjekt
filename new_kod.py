import tkinter as tk

class Ksiazki:
    def __init__(self, ksiazki):
        self.ksiazki = ksiazki
    def wyswietlKsiazki(self):
        print("Ksiązki w bibliotece: ")
        for j in self.ksiazki:
            print(j)

class Karta:
    def __init__(self, ksiazkiWypozyczone):
        self.ksiazkiWypozyczone = ksiazkiWypozyczone
    def wypozyczKsiazke(self, tytul1):
        if tytul1 in Ksiazki.ksiazki:
            Ksiazki.ksiazki.remove(tytul1)
            self.ksiazkiWypozyczone.append(tytul1)
    def wyswietlWypozyczone(self):
        print("Książki wypożyczone:")
        for i in self.ksiazkiWypozyczone:
            print(i)
    def usunKsiazki(self, tytul2):
        Ksiazki.ksiazki.remove(tytul2)
    def edytujKsiazki(self, stary_tytul, nowy_tytul):
        if stary_tytul in self.ksiazkiWypozyczone:
            self.ksiazkiWypozyczone(self.ksiazkiWypozyczone.index(stary_tytul)) = nowy_tytul


obiektKsiazki = Ksiazki(["przykksiążka", "Tak"])
obiektKarta = Karta(["przykksiążka2"])