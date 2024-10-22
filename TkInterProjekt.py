from tkinter import *
import tkinter as tk

class Ksiazki:
    def __init__(self, ksiazki):
        self.ksiazki = ksiazki
    def wyswietlKsiazki(self):
        windowWyswietlBiblioteke = Tk()
        windowWyswietlBiblioteke.title("Książki w bibliotece")
        windowWyswietlBiblioteke.geometry("500x200")

        textWyswietlBiblioteke = Text(windowWyswietlBiblioteke, height=5, width=52)
        textWyswietlBiblioteke.pack()
        textWyswietlBiblioteke.insert(tk.END, "\n".join(self.ksiazki))
        textWyswietlBiblioteke.config(state=tk.DISABLED)

        windowWyswietlBiblioteke.mainloop()

class Karta:
    def __init__(self, ksiazkiWypozyczone):
        self.ksiazkiWypozyczone = ksiazkiWypozyczone

    def wypozyczKsiazke(self, tytul1):
        if tytul1 in Ksiazki.ksiazki:
            Ksiazki.ksiazki.remove(tytul1)
            self.ksiazkiWypozyczone.append(tytul1)

    def wyswietlWypozyczone(self):
        windowWyswietlWypozyczone = Tk()
        windowWyswietlWypozyczone.title("Książki wypożyczone")
        windowWyswietlWypozyczone.geometry("500x200")

        textWyswietlWypozyczone = Text(windowWyswietlWypozyczone, height=5, width=52)
        textWyswietlWypozyczone.pack()
        textWyswietlWypozyczone.insert(tk.END, "\n".join(self.ksiazkiWypozyczone))
        textWyswietlWypozyczone.config(state=tk.DISABLED)

        windowWyswietlWypozyczone.mainloop()

    def usunKsiazki(self, tytul2):
        Ksiazki.ksiazki.remove(tytul2)

obiektKsiazki = Ksiazki(["przykksiążka", "Tak"])
obiektKarta = Karta(["przykksiążka2"])

window = Tk()
window.title("Biblioteka")
window.geometry("500x200")

def guzikWypozyczWcisniety():
    obiektKarta.wypozyczKsiazke()
guzikWypozycz = Button(window, text="Wypozycz Książkę", command=guzikWypozyczWcisniety)
guzikWypozycz.place(x=75, y=50)

def guzikWyswietlWypozyczone():
    obiektKarta.wyswietlWypozyczone()
guzikWyswietlK = Button(window, text="Wyświetl Ksiązki Wypozyczone", command=guzikWyswietlWypozyczone)
guzikWyswietlK.place(x=75, y=75)

def guzikUsunKsiazki():
    obiektKarta.usunKsiazki()
guzikWypozycz = Button(window, text="Usuń Książkę z Karty", command=guzikWypozyczWcisniety)
guzikWypozycz.place(x=75, y=100)

def guzikWyswietlBiblioteke():
    obiektKsiazki.wyswietlKsiazki()
guzikWyswietlB = Button(window, text="Wyświetl Książki z Biblioteki", command=guzikWyswietlBiblioteke)
guzikWyswietlB.place(x=75, y=125)

window.mainloop()