"""
Simple script to practice read from file, class definition.
In Czech, english version is not available.
Python.
"""

# Vytvořte třídu aut s danými parametry - znacka_auta, spz_auta, palivo_v_litrech, spotreba.
# Na vystupu vytiskněte puze udaje pro auta ze skupiny podporovanych značek -
# nactenych z externiho souboru.

with open("podporovane_znacky.txt") as soubor:
    podporovane_znacky = soubor.read().splitlines()
    print(podporovane_znacky)

class Auto:
    def __init__(self, znacka_auta, spz_auta, palivo_v_litrech, spotreba):
        self.znacka_auta = znacka_auta
        if znacka_auta not in podporovane_znacky:
            print(f"Značka auta {znacka_auta} není podporována.")
        self.spz_auta = spz_auta
        if len(spz_auta) != 7:
            print(f"SPZ {spz_auta} nemá požadovanou délku.")
        self.palivo_v_litrech = palivo_v_litrech
        if float(palivo_v_litrech) < 0:
            print(f"Množství paliva {palivo_v_litrech} nesmí být záporné.")
        self.spotreba = spotreba

auto_ford = Auto("Ford", "3SR244", "12", "6")
auto_audi = Auto("Audi", "5H69896", "-2", "5")
auto_skoda = Auto("Skoda", "6G89067", "10", "5.5")
auto_kia = Auto("Kia", "4AH0997", "12", "5")



print(auto_ford.spotreba)
print(auto_audi.palivo_v_litrech)
print(auto_skoda.znacka_auta)
print(auto_kia.spotreba)

print("Konec.")