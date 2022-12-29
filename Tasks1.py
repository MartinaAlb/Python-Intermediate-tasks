Soubor = open("podporovane_znacky.txt", "r")
povolene_znacky = Soubor.readlines()
print(repr(povolene_znacky))
Soubor.close()

class Auto:
    def __init__(self, znacka_auta, spz_auta, palivo_v_litrech, spotreba):
        self.znacka_auta = znacka_auta
        if znacka_auta not in povolene_znacky:
            print("Značka auta není podporována.")
        self.spz_auta = spz_auta
        if len(spz_auta) != 7:
            print("SPZ nemá požadovanou délku.")
        self.palivo_v_litrech = palivo_v_litrech
        if float(palivo_v_litrech) < 0:
            print("Množství paliva nesmí být záporné.")
        self.spotreba = spotreba

auto_ford = Auto("Ford\n", "3SR2844", "12", "6")
auto_audi = Auto("Audi", "5H69089", "20", "5")
auto_skoda = Auto("Skoda", "6G89067", "10", "5.5")


print(auto_ford.spotreba)
print(auto_audi.spz_auta)
print(auto_skoda.znacka_auta)

print("Konec.")