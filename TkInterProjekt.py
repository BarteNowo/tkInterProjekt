from tkinter import *
from tkinter import messagebox

class Ksiazki:
    def __init__(self, ksiazki):
        self.ksiazki = ksiazki

class Karta:
    def __init__(self, ksiazkiWypozyczone):
        self.ksiazkiWypozyczone = ksiazkiWypozyczone
    def wypozyczKsiazke(self, tytul1):
        if tytul1 in Ksiazki.ksiazki:
            Ksiazki.ksiazki.remove(tytul1)
            self.ksiazkiWypozyczone.remove(tytul1)
    def wyswietlWypozyczone(self):
        for i in self.ksiazkiWypozyczone:
            print(i)
    def usunKsiazki(self, tytul2):
        Ksiazki.ksiazki.remove(tytul2)

obiektKsiazki = Ksiazki(["przykksiążka", "Tak"])
obiektKarta = Karta(["przykksiążka2"])

window = Tk()
window.geometry("200x100")

def guzikWypozyczWcisniety():
    obiektKarta.wypozyczKsiazke()

guzikWypozycz = Button(window, text="cos", command=guzikWypozyczWcisniety)
guzikWypozycz.place(x=75, y=50)

window.mainloop()