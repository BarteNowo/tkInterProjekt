import tkinter as tk

class Ksiazki:
    def __init__(self, ksiazki):
        self.ksiazki = ksiazki

class Karta:
    def __init__(self, ksiazkiWypozyczone):
        self.ksiazkiWypozyczone = ksiazkiWypozyczone
    def wypozyczKsiazke(self, numer1):
        self.ksiazkiWypozyczone.append(Ksiazki.ksiazki[numer1])
        Ksiazki.ksiazki.remove(numer1)
    def wyswietlWypozyczone(self):
        print(self.ksiazkiWypozyczone)
    def usunKsiazki(self, numer2):
        Ksiazki.ksiazki.remove(numer2)

obiektKsiazki = Ksiazki({1 : "Życie w Nigerii",2 : "Tak"})
obiektKarta = Karta(["I'm black"])

window = tk.Tk()

greetings = tk.Label(text="Księgarnia")
greetings.pack()

def guzikWcisniety():
    print("cos")
guzik = tk.Button(window, text="cos", command=guzikWcisniety)

window.mainloop()